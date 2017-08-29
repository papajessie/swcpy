#!/usr/bin/python3


import textwrap
import sys
import json
import codecs
from datetime import date
from pprint import pprint

hq=10
side='rebel'
version=1048
verbosity=0
planet='planet1'
mode='crate'
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
        print ('--- Setting {0} to {1}'.format(configitems[x],config[x]))
    else:
        print ('--- Config item {0} unknown, ignoring'.format(x))
    
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
        displayed[category]=[]
    displayed[category].append(item)
        
def _(x):
    global langdata
    if x in langdata:
        return langdata[x]
    else:
        return '_'+x+'_ (no translation)'


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
    mode=config['mode']

    modes=mode.split(",")
    # Modes in one single phase
    xhelp['tables']='List all tables available in the data files, as well as the number of entries.'
    if ('tables' in modes):
        for t in data:
            print('{0};{1}'.format(t,len(data[t])))
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
    # Output phase
    out=[]
    outputs=config['output'].split(",")
    if ('tournament' in modes):
        if ('list' in outputs):
            output_listheader_tournament(out,objects,displayed['tournament'])
            dates={}
            for tournament in displayed['tournament']:
                dates[objects[tournament]['startDate']+objects[tournament]['endDate']+objects[tournament]['planetId']]=tournament
            for xtournament in sorted(dates):
                tournament=dates[xtournament]
                output_list_tournament(out,objects,objects[tournament])
        if ('csv' in outputs):
            output_csvheader_tournament(out,objects,displayed['tournament'])
            for tournament in displayed['tournament']:
                output_csv_tournament(out,objects,objects[tournament])
    # list mode: print output
    if ('list' in outputs):
        if (len(out)>0):
            print("\n\n".join(out))
    if ('csv' in outputs):
        if (len(out)>0):
            print("\n".join(out))
    # Help mode
    xhelp['help']='Display this help text.'
    if ('help' in modes):
        wrapper = textwrap.TextWrapper()
        wrapper.initial_indent='    '
        wrapper.subsequent_indent='    '
        morewrapper =  textwrap.TextWrapper()
        morewrapper.initial_indent='      '
        morewrapper.subsequent_indent='      '
        for k,v in xhelp.items():
            print(' * {0}'.format(k))
            print("\n".join(wrapper.wsrap(v)))
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
    if id in objects:
        return
    pass


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
        ob['endDate']=swcdatetoiso(swcitem['endDate'])
        ob['startDate']=swcdatetoiso(swcitem['startDate'])
        if 'planetId' in swcitem:
            ob['planetId']=swcitem['planetId']
        else:
            ob['planetId']='planet1'
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
                        oldplanet=''
                        if 'planet' in config:
                            oldplanet=config['planet']
                        config['planet']=ob['planetId']
                        for crate in myrew['crateRewardUid']:
                            analyse_crate(objects,displayed,crate)
                        if oldplanet != '':
                            config['planet']=oldplanet

# This set of functions output objects for various modes
def output_listheader_tournament(out,objects,displayed):
    out.append("There are {0} tournaments in the selection:".format(len(displayed)))

def output_list_tournament(out,objects,item):
    rewards=item['rewards']
    rewardsstr=''
    leagues={'tournament_tier_8':'ULTRACHROME','tournament_tier_7':'OBSIDIAN','tournament_tier_6':'BRONZIUM_01','tournament_tier_5':'BRONZIUM_02','tournament_tier_4':'DURASTEEL_02','tournament_tier_3':'DURASTEEL_01','tournament_tier_2':'CARBONITE_01','tournament_tier_1':'CARBONITE_02'}
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
    xout='\n  * A tournament "{4}" ({0}) that begins on {1} and ends on {2} on planet {3}.{5}'.format(item['uid'],item['startDate'],item['endDate'],display_planet(item['planetId']),_('tournament_title_'+item['uid']),rewardsstr)
    out[len(out)-1]+=xout

def output_csvheader_tournament(out,objects,displayed):
    out.append('#id;planet;startDate;endDate;reward1;reward2;reward3;reward4;reward5;reward6;reward7;reward8\n')

def output_csv_tournament(out,objects,item):
    rewards=item['rewards']
    ar=['','','','','','','','']
    for i in range(1,8):
        tier='tournament_tier_{0}'.format(i)
        if tier in rewards:
            ar[i-1]=','.join(rewards[tier])
    xout=";".join([item['uid'],display_planet(item['planetId']),item['startDate'],item['endDate']]+ar)
    out[len(out)-1]+=xout+'\n'


# This set of functions take an Id and return the adequate string for it
def display_planet(planetId):
    return _('planet_name_'+planetId)

def display_crate_veryshort(crateId):
    return crateId

if __name__ == "__main__":
    main(sys.argv)
