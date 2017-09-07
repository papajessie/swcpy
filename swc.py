#!/usr/bin/python3


import textwrap
import sys
import json
import codecs
import re
from datetime import date
from pprint import pprint

hq=10
side='rebel'
version=1048
verbosity=0
planet='planet1'
xdate=date.today().isoformat()

elements=[]
cratedata={}
crateitemdata={}
cratescaledata={}
basedata={}
langdata={}
data={}
config={'table':[],'lang':'en-US','output':'list'}
xhelp={}
morehelp={}
indexdata={}

def log(string):
    global config
    outputs=config['output'].split(",")
    if 'verbose' in outputs:
        print(string)

def importfile(filename):
    global config
    global data
    with open('content/{0}/patches/{1}.json'.format(config['version'],filename)) as swcfile:
        swcdata=json.load(swcfile)
        for table in swcdata['content']['objects']:
            if (not(table in data)):
                data[table]={}
            if (isinstance(swcdata['content']['objects'][table],list)):
                for item in swcdata['content']['objects'][table]:
                    if 'uid' in item:
                        uid=item['uid']
                        if (not(uid in data[table])):
                            data[table][uid]={}
                        for v in item:
                            data[table][uid][v]=item[v]
                    else:
                        print('Warning: item has no uid')
                        pprint(item)
                        sys.exit(0)
            
def importlangfile(lang):
    global config
    global langdata
    with codecs.open('content/{}/strings/strings_{}.json'.format(config['version'],lang),'r','utf-8') as stringsfile:
        langdict=json.load(stringsfile)
        for x in langdict['content']['objects']['LocalizedStrings']:
            if 'text' in x:
                langdata[x['uid']]=x['text']

def setconfig(x,y):
    global config
    configitems={'hq':'HQ level','lang':'language','side':'faction'}
    for j in ['verbosity','version','planet','mode','output','begin','end','table']:
        configitems[j]=j
    intitems=['hq','verbosity','version']
    arrayitems=['table']
    alloweditems={'side':['empire','rebel','neutral','smuggler','tusken']}
    if x in configitems:
        if ((x in alloweditems) and not(y in alloweditems[x])):
            print ('Wrong value "{0}" for setting {1}: only values accepted are {2}, ignoring.'.format(y,configitems[x],'/'.join(alloweditems[x])))
        if (x in intitems):
            config[x]=int(y)
        elif (x in arrayitems):
            if (not(x in config)):
                config[x]=[]
            config[x].append(y)
        else:
              config[x]=y
        log('--- Setting {0} to {1}'.format(configitems[x],config[x]))
    else:
        log('--- Config item {0} unknown, ignoring'.format(x))
    
def analysis(x):
    global config
    global elements
    
    a=x.split('=')
    if (len(a)==2):
        setconfig(a[0],a[1])
    else:
        elements.append(x)

def addtodisplay(displayed,category,item):
    if not(category in displayed):
        displayed[category]={}
    if item in displayed[category]:
        displayed[category][item]+=1
    else:
        displayed[category][item]=1

def getdisplayed(displayed,category):
    if not(category in displayed):
        return ()
    return (displayed[category].keys())
        


def _(x):
    global langdata
    if x in langdata:
        return langdata[x]
    else:
        return x+' (no text translation)'
def __(x):
    return display_colored(_(x))

def main(argv):
    global data
    global langdata
    global config
    global elements

    for x in sys.argv[1:]:
        analysis(x)
    if not('version' in config):
        with open('lastversion.txt') as lastversionfile:
            num=json.load(lastversionfile)
            config['version']=num
    for file in ('base','fue','olc','wts','war','reserved','cae','arc','epi','holo','prk'):
        importfile(file)
    importlangfile(config['lang'])
    if 'mode' in config:
        mode=config['mode']
    else:
        mode='help'
    xhelp['docs']='Generate all docs in Markdown format'
    if mode == 'docs':
        mode='tournament,crate'
        config['begin']='2012-01-01'
        config['output']='md'
    modes=mode.split(",")
    # Modes in one single phase
    xhelp['tables']='List all tables available in the data files, as well as the number of entries.'
    if ('tables' in modes):
        for t in data:
            print('{0};{1}'.format(t,len(data[t])))
    # Modes in one single phase
    xhelp['translate']='Searches a string ID through the SWC catalog and translates it.'
    morehelp['translate']={'':'keys to be searched'}
    if ('translate' in modes):
        for t in elements:
            print('{0};{1}'.format(t,_(t)))
    xhelp['table']='List all keys from specific tables'
    morehelp['table']={'table':'table to search keys from (cumulative, default: all tables)','':'keys to be searched'}
    if (mode == 'table'):
        tables=config['table']
        if len(tables)==0:
            tables=data.keys()
        for table in tables:
            if (not(table) in data):
                print('Table unknown {0}'.format(table))
                sys.exit(0)
            for t in data[table]:
                print('{0};{1}'.format(table,t))
    xhelp['tableitem']='List all values from specific tables (specified by table=) and specific items (no items specified is all items) in csv format'
    if (mode == 'tableitem'):
        tables=config['table']
        if len(tables)==0:
            tables=data.keys()
        for table in tables:
            if (not(table) in data):
                print('Table unknown {0}'.format(config[table]))
                sys.exit(1)
            if len(elements)==0:
                xelements=(data[table]).keys()
            else:
                xelements=elements
            for item in xelements:
                if (item in data[table]):
                    for t in data[table][item]:
                        print('{0};{1};{2};{3}'.format(table,item,t,data[table][item][t]))
    # Modes in two phases
    objects={}
    displayed={}
    # Acquisition phase
    xhelp['tournament']='Lists all tournaments (conflicts)'
    morehelp['tournament']={'begin':'Start date in format YYYY-MM-DD (default: current day)','end':'End date in format YYYY-MM-DD (default: 9999-12-31)','':'tournament identifier (default: all)'}
    if ('tournament' in modes):
        # do something that adds tournament objects
        for i in data['TournamentData']:
            analyse_tournament(objects,displayed,i)
    xhelp['crate']='List the contents of crates'
    morehelp['crate']={'planet':'planet the crate is gained from (default: all planets, as with special value "any")','hq':'hq level (default: 5 and 10)','side':'faction (default: all factions, as with special value "any")','':'crate identifier (default: all)'}
    if ('crate' in modes):
        # do something that adds tournament objects
        if len(elements)==0:
            xelements=(data['Crate']).keys()
        else:
            xelements=elements
        for i in xelements:
            analyse_crate(objects,displayed,i)
    # Output phase
    out=[]
    outputs=config['output'].split(",")
    if ('tournament' in displayed):
        if ('list' in outputs):
            output_listheader_tournament(out,objects,getdisplayed(displayed,'tournament'))
            dates={}
            for tournament in getdisplayed(displayed,'tournament'):
                dates[objects[tournament]['startDate']+objects[tournament]['endDate']+objects[tournament]['planetId']]=tournament
            for xtournament in sorted(dates):
                tournament=dates[xtournament]
                output_list_tournament(out,objects,objects[tournament])
        if ('csv' in outputs):
            output_csvheader_tournament(out,objects,getdisplayed(displayed,'tournament'))
            for tournament in getdisplayed(displayed,'tournament'):
                output_csv_tournament(out,objects,objects[tournament])
        if ('md' in outputs):
            addtodisplay(displayed,'index','tournament')
            output_mdheader_tournament(out,objects,getdisplayed(displayed,'tournament'))
            for tournament in getdisplayed(displayed,'tournament'):
                output_md_tournament(out,objects,objects[tournament])
    if ('crate' in displayed):
        if ('list' in outputs):
            output_listheader_crate(out,objects,getdisplayed(displayed,'crate'))
            for crate in sorted(getdisplayed(displayed,'crate')):
                output_list_crate(out,objects,objects[crate])
        if ('md' in outputs):
            addtodisplay(displayed,'index','crate')
            output_mdheader_crate(out,objects,getdisplayed(displayed,'crate'))
            for crate in getdisplayed(displayed,'crate'):
                output_md_crate(out,objects,objects[crate])
    if ('index' in displayed):
        id='index'
        with open("docs/{0}.md".format(id),"w") as file:
            file.write("---\ntitle: {1} ({0})\ncategory: crate\n---\n".format(id,'Main index page'))
            file.write("# {1} ({0})\n\n".format('index','Main index page'))
            for sid in sorted(getdisplayed(displayed,id)):
                title='Index of objects of type "{0}"'.format(sid)
                file.write(' * [{1}]({0}.html)\n'.format(sid,title))

    # list mode: print output
    if ('list' in outputs):
        if (len(out)>0):
            print("\n\n".join(out))
    if ('csv' in outputs):
        if (len(out)>0):
            print('\n'.join(out))
    # Help mode
    xhelp['help']='Display this help text.'
    if ('help' in modes):
        print('Usage: swc.py variable=value variable2=value2 ... item1 item2 item3 ...')
        print('Please use mode=xxx with one of these modes')
        wrapper = textwrap.TextWrapper()
        wrapper.initial_indent='    '
        wrapper.subsequent_indent='    '
        morewrapper =  textwrap.TextWrapper()
        morewrapper.initial_indent='      '
        morewrapper.subsequent_indent='      '
        for k,v in xhelp.items():
            print(' * {0}'.format(k))
            print("\n".join(wrapper.wrap(v)))
            if k in morehelp:
                for kk,vv in morehelp[k].items():
                    print("\n".join(wrapper.wrap(' - {0}{2} {1}'.format(kk,vv,('items with no xxx= specifier:' if (kk=='') else '=xxx:')))))
            
    for xmode in modes:
        if (xmode not in xhelp.keys()):
            print('Mode unknown {0}'.format(xmode))
            print("\n".join(xhelp.keys()))
    sys.exit(0)


# This set of functions builds objects from the data, gathering useful data in one place
def analyse_crate(objects,displayed,id):
    global data
    global config
    ob={}
    if id in objects:
        ob=objects[id]
    swcitem=data['Crate'][id]
    ob['uid']=swcitem['uid']
    ob['title']='crate_title_'+swcitem['uid']
    if 'expirationTime' in swcitem:
        ob['expirationTime']=swcitem['expirationTime']
    else:
        ob['expirationTime']='never'
    ob['pools']={}
    if 'variants' not in ob:
        ob['variants']={}
    if 'variantsdefaults' not in ob:
        ob['variantsdefaults']={}
    draws=0
    for x in swcitem['supplyPoolUid']:
        if x in ob['pools']:
            ob['pools'][x]+=1
            draws+=1
        else:
            ob['pools'][x]=1
            draws+=1
            if x not in ob['variants']:
                ob['variants'][x]={}
            if x not in ob['variantsdefaults']:
                ob['variantsdefaults'][x]={}
    ob['draws']=draws
    # We do not pass because of variants by hq, planet, side
    if 'side' in config:
        if config['side']=='any':
            sides=['empire','rebel']
        else:
            sides=[config['side']]
    else:
            sides=['empire','rebel']        
    if 'hq' in config:
        hqs=[config['hq']]
    else:
        hqs=[5,10]
    if 'defaultplanet' in config:
        defaultplanet=config['defaultplanet'].split(",")
    else:
        defaultplanet=[]
        for ii in data['ObjSeries']:
            i=data['ObjSeries'][ii]
            if not(i['planetUid'] in defaultplanet):
                defaultplanet.append(i['planetUid'])
        defaultplanet=sorted(defaultplanet)
        config['defaultplanet']=",".join(defaultplanet)
    if 'planet' in config:
        if config['planet']=='any':
            planets=defaultplanet
        else:
            planets=[config['planet']]
    else:
            planets=defaultplanet
    for planet in planets:
        for hq in hqs:
            for side in sides:
                variant='{2},{1},{0}'.format(planet,hq,side)
                if variant not in ob['variants']:
                    analyse_crate_variant(objects,displayed,id,ob,variant,planet,hq,side)
    addtodisplay(displayed,'crate',id)
    if id not in objects:
        objects[id]=ob
    
def analyse_crate_variant(objects,displayed,id,ob,variant,planet,hq,side):
    global data
    global config
    # Fill in pools for specific values of planet, hq, side
    for pool in ob['pools'].keys():
        sensitive={}
        pools={}
        flat=1
        defaults={}
        if 'fallbackUid' in data['CrateSupplyPool'][pool]:
            (fflat,defaults)=analyse_cratepoolitem(hq,data['CrateSupply'][data['CrateSupplyPool'][pool]['fallbackUid']])
        variant='{2},{1},{0}'.format(planet if 'planet' in sensitive else 'any',hq if (fflat==0) else 'any',side if 'faction' in sensitive else 'any')
        ob['variantsdefaults'][pool][variant]=defaults
        instances=0
        for i in data['CrateSupply']:
            item=data['CrateSupply'][i]
            if ('crateSupplyPoolUid' in item) and (pool in item['crateSupplyPoolUid']):
                if ('maxHQ' in item and hq > int(item['maxHQ'])):
                    sensitive['hq']=1
                    continue
                if ('minHQ' in item and hq < int(item['minHQ'])):
                    sensitive['hq']=1
                    continue
                if ('faction' in item and side != item['faction']):
                    sensitive['faction']=1
                    continue
                if ('planet' in item and planet not in item['planet']):
                    sensitive['planet']=1
                    continue
                (xflat,pools[item['uid']])=analyse_cratepoolitem(hq,item)
                if xflat==0:
                    flat=0
                inst=1
                if 'poolInstances' in item:
                    inst=int(item['poolInstances'])
                pools[item['uid']]['rate']=inst
                instances+=inst
        if (flat==0):
            sensitive['hq']=1
        variant='{2},{1},{0}'.format(planet if 'planet' in sensitive else 'any',hq if 'hq' in sensitive else 'any',side if 'faction' in sensitive else 'any')
        ob['variants'][pool][variant]={'items': pools,'instances':instances}

def analyse_cratepoolitem(hq,item):
    global data
    simple_item={}
    simple_item['rewardType']=item['rewardType']
    simple_item['rewardUid']=item['rewardUid']
    flat=1
    if 'scalingUid' in item:
        scale=item['scalingUid']
        xnum=data['CrateSupplyScale'][scale]['HQ10']
        for k in data['CrateSupplyScale'][scale]:
            if data['CrateSupplyScale'][scale][k]!=xnum:
                flat=0
        num=data['CrateSupplyScale'][scale]['HQ{0}'.format(hq)]
    elif 'amount' in item:
        num=item['amount']
    else:
        num='???'
    simple_item['num']=num
    return(flat,simple_item)

def analyse_tournament(objects,displayed,id):
    global data
    global config
    if id in objects:
        return
    ob={}
    def swcdatetoiso(x):
        a=x.split(",")[1]
        (b,c,d)=a.split('-')
        return '{2}-{1}-{0}'.format(b,c,d)
    if id in data['TournamentData']:
        swcitem=data['TournamentData'][id]
        ob['uid']=swcitem['uid']
        ob['title']='tournament_title_'+swcitem['uid']
        ob['endDate']=swcdatetoiso(swcitem['endDate'])
        ob['startDate']=swcdatetoiso(swcitem['startDate'])
        if 'planetId' in swcitem:
            ob['planetId']=swcitem['planetId']
        else:
            ob['planetId']='planet1'
        if 'planet' in config:
            if config['planet']!=ob['planetId']:
                return
        localsd=date.today().isoformat()
        if 'begin' in config:
            localsd=config['begin']
        if 'end' in config:
            localed=config['end']
        else:
            localed='2999-12-31'
        rew={}
        ob['rewards']=rew
        if (ob['startDate']<=localed and ob['endDate']>=localsd):
            addtodisplay(displayed,'tournament',id)
            objects[id]=ob
            if 'rewardGroupId' in swcitem:
                rewardgroup=swcitem['rewardGroupId']
                for rewards in data['TournamentRewards']:
                    if (data['TournamentRewards'][rewards]['tournamentRewardsId'] == rewardgroup):
                        myrew=data['TournamentRewards'][rewards]
                        rew[myrew['tournamentTier']]=myrew['crateRewardUid']
                        oldplanet='any'
                        if 'planet' in config:
                            oldplanet=config['planet']
                        config['planet']=ob['planetId']
                        for crate in myrew['crateRewardUid']:
                            analyse_crate(objects,displayed,crate)
                        if oldplanet != 'any':
                            config['planet']=oldplanet
                        else:
                            del config['planet']

# This set of functions output objects for various modes
def output_listheader_crate(out,objects,displayed):
    out.append("There are {0} crates in the selection:".format(len(displayed)))

def output_list_crate(out,objects,item,LINKS=False):
    id=item['uid']
    title=__(item['title'])
    xout='\n# {1} ({0})\n\n'.format(id,title)
    xout+='Crates are given as rewards for various actions. The content is revealed only when opening them, by drawing once (or more) in various prize pools. Only one prize is won for each pool per draw. The in-game description of expectations is written manually and can be wrong. The probability of obtaining one prize is indicated below; the pools change according to planet, faction and HQ level.\n\n'
    expiration=display_expiration(item['expirationTime'])
    if (expiration == 'never'):
        xout+='This crates does not expire.'
    else:
        xout+='This crate expires after {0}.'.format(expiration)
    draws=item['draws']
    pools=item['pools']
    if (draws==1):
        xout+=' The contents are one draw from one pool only.'
    elif (draws==len(pools)):
        xout+=' The contents are one draw from each of the {0} pools.'.format(len(pools))
    elif (pools==1):
        xout+=' The contents are {0} draws from one pool.'.format(draws)
    else:
        xout+=' The contents are decided by {0} draws from {1} different pools.'.format(draws,len(pools))
        for i in sorted(pools.keys()):
            xout+='\n  * {0} draw{2} from pool "{1}"'.format(pools[i],i,'s' if pools[i]>1 else '')
    for j in sorted(pools.keys()):
        xout+='\n\n## Pool "{0}" (x{1} draw{2})'.format(j,pools[j],'' if pools[j]<2 else 's')
        for i in sorted(item['variants'][j]):
            xout+='\n\n### {0}\n'.format(display_poolvariant(i))
            instances=item['variants'][j][i]['instances']
            lines=[]
            if (instances==0):
                lines.append('  * No items, see the fallback option below')
            for it in item['variants'][j][i]['items']:
                myit=item['variants'][j][i]['items'][it]
                lines.append('  * ({0}/{1}) {2}'.format(myit['rate'],instances,display_unitbatch(myit,LINKS)))
            xout+='\n'+'\n'.join(sorted(lines))
        for i in sorted(item['variantsdefaults'][j]):
            xout+='\n\n### Fallback{0}\n'.format(display_poolvariant(i,False))
            myit=item['variantsdefaults'][j][i]
            xout+='\n  * {0}'.format(display_unitbatch(myit,LINKS))
    out[len(out)-1]+=xout

def output_listheader_tournament(out,objects,displayed):
    out.append("There are {0} tournaments in the selection:".format(len(displayed)))

def output_list_tournament(out,objects,item):
    rewards=item['rewards']
    rewardsstr=''
    leagues={'tournament_tier_8':'ULTRACHROME','tournament_tier_7':'OBSIDIAN','tournament_tier_6':'BRONZIUM_01','tournament_tier_5':'BRONZIUM_02','tournament_tier_4':'DURASTEEL_01','tournament_tier_3':'DURASTEEL_02','tournament_tier_2':'CARBONITE_01','tournament_tier_1':'CARBONITE_02'}
    if len(rewards)>0:
        rewardsstr=' The rewards are:'
        for k in sorted(rewards.keys()):
            if len(rewards[k])==1:
                rewardsstr+='\n    * {1}: crate "{2}"'.format(k,_('TOURNAMENT_TIER_'+leagues[k]),rewards[k][0])
            else:
                rewardsstr+='\n    * {1}: '.format(k,_('TOURNAMENT_TIER_'+leagues[k]))
                crates={}
                for j in rewards[k]:
                    if j in crates:
                        crates[j]+=1
                    else:
                        crates[j]=1
                for j,k in crates.items():
                    if k==1:
                        rewardsstr+='crate "{1}"'.format(k,display_crate_veryshort(j))
                    else:
                        rewardsstr+='{0} crates "{1}"'.format(k,display_crate_veryshort(j))
                rewardsstr+=''
    xout='\n  * A tournament "{4}" ({0}) that begins on {1} and ends on {2} on planet {3}.{5}'.format(item['uid'],item['startDate'],item['endDate'],display_planet(item['planetId']),_(item['title']),rewardsstr)
    out[len(out)-1]+=xout

def output_csvheader_tournament(out,objects,displayed):
    out.append('#id;planet;startDate;endDate;reward1;reward2;reward3;reward4;reward5;reward6;reward7;reward8')

def output_csv_tournament(out,objects,item):
    rewards=item['rewards']
    ar=['','','','','','','','']
    for i in range(1,9):
        tier='tournament_tier_{0}'.format(i)
        if tier in rewards:
            ar[i-1]=','.join(rewards[tier])
        else:
            print('no reward '+tier)
    xout=";".join([item['uid'],display_planet(item['planetId']),item['startDate'],item['endDate']]+ar)
    out[len(out)-1]+='\n'+xout

def output_mdheader_tournament(out,objects,displayed):
    with open("docs/tournament.md","w") as file:
        file.write("---\ntitle: Index of conflicts\n---\n")
        file.write("# Conflicts\n\n")
        dates={}
        for tournament in displayed:
            dates[objects[tournament]['startDate']+objects[tournament]['endDate']+objects[tournament]['planetId']]=tournament
        for xtournament in reversed(sorted(dates)):
            tournament=dates[xtournament]
            item=objects[tournament]
            id=item['uid']
            title=__(item['title'])
            file.write("  * [{1} ({0})]({0}.html)\n".format(id,title))

def output_md_tournament(out,objects,item):
    id=item['uid']
    title=__('tournament_title_'+id)
    with open("docs/{0}.md".format(id),"w") as file:
        file.write("---\ntitle: {1} ({0})\ncategory: tournament\n---\n".format(id,title))
        file.write("# {0}\n\n  * Start date: {1}\n  * End date: {2}\n\n".format(title,item['startDate'],item['endDate']))
        file.write("## Rewards\n\n")
        rewards=item['rewards']
        rewardsstr=''
        leagues={'tournament_tier_8':'ULTRACHROME','tournament_tier_7':'OBSIDIAN','tournament_tier_6':'BRONZIUM_01','tournament_tier_5':'BRONZIUM_02','tournament_tier_4':'DURASTEEL_02','tournament_tier_3':'DURASTEEL_01','tournament_tier_2':'CARBONITE_01','tournament_tier_1':'CARBONITE_02'}
        if len(rewards)>0:
            for k in sorted(rewards.keys()):
                file.write('  * {1}:'.format(k,_('TOURNAMENT_TIER_'+leagues[k])))
                crates={}
                for j in rewards[k]:
                    if j in crates:
                        crates[j]+=1
                    else:
                        crates[j]=1
                head=' '
                if len(crates.keys())>1:
                    file.write('\n')
                    head='    * '
                for j,k in crates.items():
                    if k==1:
                        file.write(head+'A "{1}"'.format(k,display_crate_mdlink(j,'')))
                    else:
                        file.write(head+'{0} "{1}"'.format(k,display_crate_mdlink(j,'s')))
                file.write('\n')
            file.write(rewardsstr)
    

def output_mdheader_crate(out,objects,displayed):
    with open("docs/crate.md","w") as file:
        file.write("---\ntitle: Index of crates\n---\n")
        file.write("# Crates\n\n")
        dates={}
        for crate in displayed:
            item=objects[crate]
            id=item['uid']
            title=__(item['title'])
            file.write("  * [{1} ({0})]({0}.html)\n".format(id,title))

def output_md_crate(out,objects,item):
    id=item['uid']
    title=__(item['title'])
    with open("docs/{0}.md".format(id),"w") as file:
        file.write("---\ntitle: {1} ({0})\ncategory: crate\n---\n".format(id,title))
        lout=['']
        output_list_crate(lout,objects,item,True)
        file.write(lout[0])


# This set of functions take an Id and return the adequate string for it

def display_planet(planetId):
    return _('planet_name_'+planetId)

def display_side(side):
    if (side=='empire'):
        return 'Empire'
    if (side=='rebel'):
        return 'Rebellion'
    return side

def display_crate_veryshort(crateId):
    return crateId

def display_crate_mdlink(crateId,plural):
    return '[{1}{2} ({0})]({0}.html)'.format(crateId,_('crate_title_'+crateId),plural)

def display_colored(string):
        return re.sub("\[.*\]", '', string)

def display_expiration(s):
    if (s=='never'):
        return s
    a=int(s)
    days=int(a/1440)
    hours=int((a%1440)/60)
    minutes=int(a%60)
    x=''
    if days>0:
        x='{0}d'.format(days)
    if (hours+minutes)>0:
        x+='{0:02d}h'.format(hours)
    if minutes>0:
        x+='{0:02d}m'.format(minutes)
    return x

def display_poolvariant(s,cap=True):
    (side,hq,planet)=s.split(',')
    if side=='any':
        if planet=='any':
            if hq=='any':
                if cap:
                    return 'Always'
                else:
                    return ''
            else:
                if cap:
                    return 'With HQ level {0}'.format(hq)
                else:
                    return ' with HQ level {0}'.format(hq)
        else:
            return '{2}n planet {0}{1}'.format(display_planet(planet),'' if hq=='any' else ', with HQ level {0}'.format(hq),'O' if cap else ' o')
    else:
        return '{3}{2}{0}{1}'.format('' if planet=='any' else ', on planet {0}'.format(display_planet(planet)),'' if hq=='any' else ', with HQ level {0}'.format(hq),display_side(side),'' if cap else ' for the ')
    return '{2}, on planet {0} with HQ level {1}'.format(display_planet(planet),hq,display_side(side),'' if cap else ' for the ')

def display_unitbatch(item,link):
    count=item['num']
    nature=''
    itemx=''
    title=''
    line='{0} {1} {2}'
    if link:
        line='{0} {1} [{2}]({3})'
    if (item['rewardType'] == 'currency'):
        array={'contraband': _('CONTRABAND'), 'crystals':_('CRYSTALS'),'materials':_('MATERIALS'),'credits':_('CREDITS'), 'reputation':_('REPUTATION')}
        nature='resource'
        itemx=array[item['rewardUid']]
        line='{0} {3}'
    elif (item['rewardType'] == 'shard'):
        nature='data fragments of equipment'
        itemx=item['rewardUid']
        title=_(display_things(item['rewardUid'],'EquipmentData','equipmentID','equipmentName'))
    elif (item['rewardType'] == 'shardTroop'):
        nature='data fragments of unlockable troop'
        itemx=display_things(item['rewardUid'],'TroopData','upgradeShardUid','unitID')
        title=_('trp_title_'+itemx)
    elif (item['rewardType'] == 'shardSpecialAttack'):
        nature='data fragments of unlockable air support'
        itemx=display_things(item['rewardUid'],'SpecialAttackData','upgradeShardUid','specialAttackID')
        title=_('shp_title_'+itemx)
    elif (item['rewardType'] == 'troop'):
        nature='troop sample'
        itemx=display_things(item['rewardUid'],'TroopData','uid','unitID')
        title=_('trp_title_'+itemx)
    elif (item['rewardType'] == 'specialAttack'):
        nature='air support sample'
        itemx=display_things(item['rewardUid'],'SpecialAttackData','uid','specialAttackID')
        title=_('shp_title_'+itemx)
    elif (item['rewardType'] == 'hero'):
        nature='hero sample of'
        itemx=display_things(item['rewardUid'],'TroopData','uid','unitID')
        title=_('trp_title_'+itemx)
    else:
        nature=item['rewardType']
        itemx=name
        line='{0} {1}: {2}'
    if title=='':
        title=itemx
    line=line.format(count,nature,title,itemx)
    return(line)

def display_things(uid,table,localid,localname):
    global data
    for xx in data[table]:
        x=data[table][xx]
        if ((localid in x) and (localname in x) and (x[localid]==uid)):
            return x[localname]
    return uid

if __name__ == "__main__":    
    main(sys.argv)
