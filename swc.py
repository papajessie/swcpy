#!/usr/bin/python3


import textwrap
import sys
import json
import codecs
import re
import hashlib
from datetime import date
from pprint import pprint
import os
import shutil

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
config['stattranslation']={}
config['stattype']={}
config['stathandler']={}
config['buffs']={}

xhelp={}
morehelp={}
indexdata={}

def log(string):
    global config
    outputs=config['output'].split(",")
    if 'verbose' in outputs:
        print(string)

def die(string,item=None):
    print(string)
    if item is not None:
        pprint(item)
    sys.exit(0)
    
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
                        die('Item has no uid',item=item)
            
def importlangfile(lang):
    global config
    global langdata
    with codecs.open('content/{}/strings/strings_{}.json'.format(config['version'],lang),'r','utf-8') as stringsfile:
        langdict=json.load(stringsfile)
        for x in langdict['content']['objects']['LocalizedStrings']:
            if 'text' in x:
                langdata[x['uid']]=x['text']
    with codecs.open('content/{}/strings/strings-hn_{}.json'.format(config['version'],lang),'r','utf-8') as stringsfile:
        langdict=json.load(stringsfile)
        for x in langdict['content']['objects']['LocalizedStrings']:
            if 'text' in x:
                langdata[x['uid']]=x['text']


def camel_case_to_phrase(s):
    prev = None
    t = []
    n = len(s)
    i = 0
    while i < n:
        next_char = s[i+1] if i < n -1 else ''
        c = s[i]
        if prev is None:
            t.append(c.upper())
        elif c.isupper() and prev.isupper():
            if next_char.islower():
                t.append(' ')
                t.append(c.lower())
            else:
                t.append(c)
        elif c.isupper() and not prev.isupper():
            t.append(' ')
            if next_char.islower():
                t.append(c.lower())
            else:
                t.append(c)
        else:
            t.append(c)
        prev = c
        i = i +1
    return "".join(t)

def prependlower(pr,c):
    if len(pr)>0:
        if len(c)<2:
            c=pr+c
        elif c[:2].upper()==c[:2]:
            c=pr+c
        else:
            c=pr+c[:1].lower()+c[1:]
    return(c)

def dget(array,key,default):
    a=default
    try:
        a=array[key]
        return a
    except KeyError:
        return default


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
    return sorted(displayed[category].keys())
        
def initstat():
    global config
    config['statopt']={}
    config['stattranslation']={
        'bruiserInfantry':'Heavy infantry',
        'bruiserVehicle':'Heavy vehicle',
        'building':'Other building',
        'champion':'Droideka',
        'flierInfantry':'Flying infantry',
        'flierVehicle':'Flying vehicle',
        'healerInfantry':'Support troop',
        'heroBruiserInfantry':'Heavy infantry hero',
        'heroBruiserVehicle':'Heavy vehicule hero',
        'heroInfantry':'Infantry hero',
        'heroVehicle':'Vehicule hero',
        'HQ':'Headquarters',
        'infantry':'Infantry',
        'turret':'Turret',
        'trap':'Trap',
        'shield':'Shield',
        'resource':'Ressource generator',
        'vehicle':'Light vehicle',
        'size':'Unit capacity',
        'levels':'Levels available',
        'playerFacing': 'Buildable unit',
        'upgrade': 'Upgrade requirements',
        'damage':'Damage per shot',
        'dps':'Displayed damage per second',
        'faction':'Side',
        'overWalls':'Can shoot over walls',
        'selfCenteredTargeting':'Self-centered targeting',
        'trains':'Training cost',
        'isFlying':'Flying unit',
        'sizes':'Size',
        'pathSearchWidth':'Propensity to go around obstacles',
        'gunSequence':'Gun shooting sequence',
        'shotDelay':'Time between shots',
        'chargeTime':'Time between start of clip and first shot',
        'cooldownTime':'Supplementary time between last shot and reload',
        'reload':'Time between end of clip and start of clip',
        'preventDonation': 'Can be given',
        'targets':'Target preferences',
        'upgrades':'Upgrade requirements',
        'sizes':'Unit size on map',
        'uiDecalAssetName': 'UI decal asset name',
        'projectile:DPS': 'Calculated damage per second',
        'projectile:mults': 'Damage multipliers',
        '':''
    }
    config['statrole']={
        # Below are synthetic values
        'sizes': 'move',
        'targets': 'attackmove',
        'trains': 'xtrain',
        'upgrades': 'xupgrade',
        'buffHealth': 'buffbasic',
        'projectile:mults': 'projectilemisc',
        'buff:name': 'buffbasic',
        'buff:summon visitors': 'buffbasic',
        # Below are values reserved to units
        'ability': 'internal',
        'acceleration': 'move',
        'armorType': 'basic',
        'assetName': 'presentation',
        'attackShieldBorder': 'attackmove',
        'audioAttack': 'presentation',
        'audioDeath': 'presentation',
        'audioImpact': 'presentation',
        'audioPlacement': 'presentation',
        'audioTrain': 'presentation',
        'autoSpawnRateScale': 'unknown',
        'autoSpawnSpreadingScale': 'unknown',
        'buffAssetOffset': 'presentation',
        'bundleName': 'presentation',
        'contraband': 'train',
        'credits': 'train',
        'crushesWalls': 'move',
        'deathAnimation': 'presentation',
        'deathProjectile': 'internal',
        'deathProjectileDamage': 'deathprojectilebasic',
        'deathProjectileDelay': 'deathbasic',
        'deathProjectileDistance': 'deathbasic',
        'decalAssetName': 'presentation',
        'decalBundleName': 'presentation',
        'decalSize': 'presentation',
        'effectType': 'presentation',
        'eventButtonAction': 'presentation',
        'eventButtonData': 'presentation',
        'eventButtonString': 'presentation',
        'eventFeaturesString': 'presentation',
        'faction': 'basic',
        'factoryRotation': 'presentation',
        'factoryScaleFactor': 'presentation',
        'gunPosition': 'presentation',
        'health': 'basic',
        'heroData': 'internal',
        'hologramUid': 'presentation',
        'iconCameraPosition': 'presentation',
        'iconCloseupCameraPosition': 'presentation',
        'iconCloseupLookatPosition': 'presentation',
        'iconLookatPosition': 'presentation',
        'iconUnlockPosition': 'presentation',
        'iconUnlockRotation': 'presentation',
        'iconUnlockScale': 'presentation',
        'ignoresWalls': 'move',
        'infoUIType': 'presentation',
        'isFlying': 'move',
        'lvl': 'nodisplay',
        'materials': 'train',
        'maxScale': 'unknown',
        'order': 'unknown',
        'pathSearchWidth': 'move',
        'playerFacing': 'basic',
        'pointValue': 'unknown',
        'preventDonation': 'basic',
        'requirements': 'nodisplay',
        'role': 'basic',
        'rotationSpeed': 'move',
        'runSpeed': 'move',
        'runThreshold': 'move',
        'shieldAssetName': 'presentation',
        'shieldCooldown': 'basic',
        'shieldHealth': 'basic',
        'shieldRange': 'basic',
        'size': 'basic',
        'sizex': 'nodisplay',
        'sizey': 'nodisplay',
        'spawnApplyBuffs': 'internal',
        'spawnEffectUid': 'presentation',
        'splash': 'unknown',
        'supportFollowDistance': 'move',
        'targetedType': 'presentation',
        'targetInRangeModifier': 'unknown',
        'targetPreferenceString': 'nodisplay',
        'tooltipHeightOffset': 'presentation',
        'trainingTime': 'xtrain',
        'type': 'basic',
        'uiDecalAssetName': 'presentation',
        'unitID': 'internal',
        'unlockedByEvent': 'presentation',
        'unlockedByCampaign': 'presentation',
        'unlockedByTournament': 'presentation',
        'unlockPlanet': 'basic',
        'upgradeContraband': 'upgrade',
        'upgradeCredits': 'upgrade',
        'upgradeMaterials': 'upgrade',
        'upgradeShards': 'upgrade',
        'upgradeShardUid': 'internal',
        'upgradeTime': 'xupgrade',
        'xp': 'unknown',
        # Below are values reserved to abilities or units
        'animationDelay': 'attackpresentation',
        'armingDelay': 'attackunknown',
        'bruiserInfantry': 'attackprefs',
        'bruiserVehicle': 'attackprefs',
        'building': 'attackprefs',
        'champion': 'attackprefs',
        'chargeTime': 'attackstats',
        'clipRetargeting': 'attackstats',
        'damage': 'attackstats',
        'dps': 'attackpresentation',
        'favoriteTargetType': 'attackpresentation',
        'flierInfantry': 'attackprefs',
        'flierVehicle': 'attackprefs',
        'gunSequence': 'attackstats',
        'healerInfantry': 'attackprefs',
        'heroBruiserInfantry': 'attackprefs',
        'heroBruiserVehicle': 'attackprefs',
        'heroInfantry': 'attackprefs',
        'heroVehicle': 'attackprefs',
        'HQ': 'attackprefs',
        'impactDelay': 'attackstats',
        'infantry': 'attackprefs',
        'maxAttackRange': 'attackmove',
        'maxSpeed': 'move',
        'minAttackRange': 'attackmove',
        'newTargetOnReload': 'attackstats',
        'newRotationSpeed': 'attackmove',
        'overWalls': 'attackstats',
        'projectileType': 'nodisplay',
        'reload': 'attackstats',
        'resource': 'attackprefs',
        'retargetingOffset': 'attackstats',
        'selfCenteredTargeting': 'attackstats',
        'shield': 'attackprefs',
        'shieldGenerator': 'attackprefs',
        'shotCount': 'attackstats',
        'shotDelay': 'attackstats',
        'storage': 'attackprefs',
        'strictCoolDown': 'attackunknown',
        'targetLocking': 'attackstats',
        'targetPreferenceStrength': 'attackmove',
        'trap': 'attackprefs',
        'turret': 'attackprefs',
        'uid': 'nodisplay',
        'vehicle': 'attackprefs',
        'viewRange': 'attackmove',
        'wall': 'attackprefs',
        # below are values reserved to abilities
        'ability:uid': 'nodisplay',
        'ability:projectileType': 'internal',
        'ability:altGunLocators': 'abilitypresentation',
        'ability:audioAbilityActivate': 'abilitypresentation',
        'ability:audioAbilityAttack': 'abilitypresentation',
        'ability:audioAbilityLoop': 'abilitypresentation',
        'ability:auto': 'abilityonly',
        'ability:clipCount': 'abilityunknown',
        'ability:cooldownOnSpawn': 'abilityonly',
        'ability:cooldownTime': 'abilityonly',
        'ability:description': 'abilityonly',
        'ability:duration': 'abilityonly',
        'ability:killCooldownReset': 'abilityunknown',
        'ability:maxSpeed': 'abilityunknown',
        'ability:name': 'abilitypresentation',
        'ability:persistentEffect': 'abilitypresentation',
        'ability:persistentScaling': 'abilitypresentation',
        'ability:selfBuff': 'internal',
        'ability:recastAbility': 'abilityonly',
        'ability:targetSelf': 'abilityonly',
        'ability:weaponTrailFXParams': 'abilitypresentation',
        # below are roles for projectiles
        'projectile:bruiserInfantry': 'projectilemult',
        'projectile:bruiserVehicle': 'projectilemult',
        'projectile:building': 'projectilemult',
        'projectile:champion': 'projectilemult',
        'projectile:flierInfantry': 'projectilemult',
        'projectile:flierVehicle': 'projectilemult',
        'projectile:healerInfantry': 'projectilemult',
        'projectile:heroBruiserInfantry': 'projectilemult',
        'projectile:heroBruiserVehicle': 'projectilemult',
        'projectile:heroInfantry': 'projectilemult',
        'projectile:heroVehicle': 'projectilemult',
        'projectile:HQ': 'projectilemult',
        'projectile:infantry': 'projectilemult',
        'projectile:resource': 'projectilemult',
        'projectile:shield': 'projectilemult',
        'projectile:shieldGenerator': 'projectilemult',
        'projectile:storage': 'projectilemult',
        'projectile:trap': 'projectilemult',
        'projectile:turret': 'projectilemult',
        'projectile:vehicle': 'projectilemult',
        'projectile:wall': 'projectilemult',
        'projectile:applyBuffs': 'internal',
        'projectile:arcs': 'projectilepresentation',
        'projectile:beamDamage': 'projectilebasic',
        'projectile:bullet': 'projectilepresentation',
        'projectile:chargeAssetName': 'projectilepresentation',
        'projectile:directional': 'projectilemisc',
        'projectile:groundBullet': 'projectilepresentation',
        'projectile:hitSpark': 'projectilepresentation',
        'projectile:isDeflectable': 'projectilemisc',
        'projectile:lengthSegments': 'projectilemisc',
        'projectile:maxScale': 'projectilepresentation',
        'projectile:maxSpeed': 'projectilemisc',
        'projectile:muzzleFlash': 'projectilepresentation',
        'projectile:muzzleFlashFadeTime': 'projectilepresentation',
        'projectile:name': 'projectilepresentation',
        'projectile:passThroughShield': 'projectilemisc',
        'projectile:projectileDamagePercentString': 'nodisplay',
        'projectile:projectileLength': 'projectilepresentation',
        'projectile:s1Time': 'projectileunknown',
        'projectile:s2Time': 'projectileunknown',
        'projectile:seeksTarget': 'projectileunknown',
        'projectile:spinSpeed': 'projectilepresentation',
        'projectile:splashDamagePercentages': 'projectilebasic',
        'projectile:sTransition': 'projectilepresentation',
        'projectile:streams': 'projectileunknown',
        'projectile:uid': 'nodisplay',
        'projectile:widthSegments': 'projectilemisc',
        'projectile:cannonsPerSequence': 'projectilemisc',
        'projectile:salvos': 'projectilemisc',
        'projectile:cliptime': 'projectilemisc',
        'projectile:DPS': 'projectilebasic',
        # below are roles for buffs
        'buff:applyValueAs': 'buffbasic',
        'buff:buffID': 'buffbasic',
        'buff:duration': 'buffbasic',
        'buff:lvl': 'buffbasic',
        'buff:modifier': 'buffbasic',
        'buff:msFirstProc': 'buffbasic',
        'buff:msPerProc': 'buffbasic',
        'buff:stack': 'buffbasic',
        'buff:target': 'buffbasic',
        'buff:mults': 'buffbasic',
        'buff:uid': 'buffnodisplay',
        'buff:value': 'buffbasic',
        'buff:bruiserInfantry': 'buffmult',
        'buff:bruiserVehicle': 'buffmult',
        'buff:building': 'buffmult',
        'buff:champion': 'buffmult',
        'buff:flierInfantry': 'buffmult',
        'buff:flierVehicle': 'buffmult',
        'buff:healerInfantry': 'buffmult',
        'buff:heroBruiserInfantry': 'buffmult',
        'buff:heroBruiserVehicle': 'buffmult',
        'buff:heroInfantry': 'buffmult',
        'buff:heroVehicle': 'buffmult',
        'buff:HQ': 'buffmult',
        'buff:infantry': 'buffmult',
        'buff:resource': 'buffmult',
        'buff:shield': 'buffmult',
        'buff:shieldGenerator': 'buffmult',
        'buff:storage': 'buffmult',
        'buff:trap': 'buffmult',
        'buff:turret': 'buffmult',
        'buff:vehicle': 'buffmult',
        'buff:wall': 'buffmult',
        'buff:tags': 'buffunknown',
        'buff:isRefreshing': 'buffunknown',
        'buff:details': 'buffinternal',
        'buff:shaderOverride': 'buffunknown',
        'buff:assetOffsetType': 'buffunknown',
        'buff:bundleName': 'buffpresentation',
        'buff:assetName': 'buffpresentation',
        'buff:cancelTags': 'buffunknown',
        'buff:audioAbilityEvent': 'buffpresentation',
        'buff:assetProfile': 'buffpresentation',
        'buff:projectileAttachmentBundle': 'buffpresentation',
        'buff:preventTags': 'buffunknown',
        'buff:impactAssetNameRebel': 'buffpresentation',
        'buff:impactAssetNameEmpire': 'buffpresentation',
        'buff:muzzleAssetNameRebel': 'buffpresentation',
        'buff:muzzleAssetNameEmpire': 'buffpresentation',
        # below are roles for summon details
        'buff:summon dieWithSummoner': 'buffdetails',
        'buff:summon maxProc': 'buffdetails',
        'buff:summon randomSpawnRadius': 'buffdetails',
        'buff:summon sameTeam': 'buffdetails',
        'buff:summon spawnPoints': 'buffdetails',
        'buff:summon targetSummoner': 'buffdetails',
        'buff:summon uid': 'buffinternal',
        'buff:summon visitorType': 'buffdetails',
        'buff:summon visitorUids': 'buffdetails',
        # placeholder
        '':''
        }

    keys=[x for x in config['statrole'].keys()]
    config['stattype']={
        'acceleration': 'int',
        'attackShieldBorder': 'boolean',
        'autoSpawnRateScale': 'int',
        'autoSpawnSpreadingScale': 'int',
        'contraband': 'int',
        'credits': 'int',
        'crushesWalls': 'boolean',
        'deathProjectileDamage': 'int',
        'deathProjectileDelay': 'microtime',
        'deathProjectileDistance': 'int',
        'faction': 'side',
        'health': 'int',
        'buffHealth': 'int',
        'ignoresWalls': 'boolean',
        'isFlying': 'boolean',
        'lvl': 'int',
        'materials': 'int',
        'maxScale': 'boolean',
        'pathSearchWidth': 'int',
        'playerFacing': 'boolean',
        'pointValue': 'float',
        'preventDonation': 'boolean',
        'requirements': 'array',
        'rotationSpeed': 'float',
        'runSpeed': 'int',
        'runThreshold': 'int',
        'shieldCooldown': 'time',
        'shieldHealth': 'int',
        'shieldRange': 'int',
        'size': 'int',
        'sizex': 'int',
        'sizey': 'int',
        'supportFollowDistance': 'int',
        'targetInRangeModifier': 'int',
        'trainingTime': 'time',
        'unlockPlanet': 'translate',
        'upgradeContraband': 'int',
        'upgradeCredits': 'int',
        'upgradeMaterials': 'int',
        'upgradeShards': 'int',
        'upgradeTime': 'time',
        'xp': 'int',
        'armingDelay': 'int',
        'chargeTime': 'microtime',
        'clipRetargeting': 'boolean',
        'damage': 'int',
        'dps': 'float',
        'maxAttackRange': 'int',
        'maxSpeed': 'int',
        'minAttackRange': 'int',
        'newRotationSpeed': 'float',
        'overWalls': 'boolean',
        'reload': 'microtime',
        'retargetingOffset': 'int',
        'selfCenteredTargeting': 'boolean',
        'shotCount': 'int',
        'shotDelay': 'microtime',
        'impactDelay': 'microtime',
        'strictCoolDown': 'boolean',
        'targetLocking': 'boolean',
        'targetPreferenceStrength': 'int',
        'viewRange': 'int',
        'newTargetOnReload': 'boolean',
        'unlockedByCampaign': 'boolean',
        'unlockedByTournament': 'boolean',
        'ability:auto': 'boolean',
        'ability:clipCount': 'int',
        'ability:cooldownOnSpawn': 'boolean',
        'ability:cooldownTime': 'microtime',
        'ability:duration': 'microtime',
        'ability:killCooldownReset': 'boolean',
        'ability:maxSpeed': 'int',
        'ability:persistentScaling': 'int',
        'ability:recastAbility': 'boolean',
        'ability:targetSelf': 'boolean',
        'projectile:arcs': 'boolean',
        'projectile:beamDamage': 'int',
        'projectile:directional': 'boolean',
        'projectile:isDeflectable': 'boolean',
        'projectile:maxScale': 'int',
        'projectile:maxSpeed': 'int',
        'projectile:passThroughShield': 'boolean',
        'projectile:projectileLength': 'int',
        'projectile:s1Time': 'microtime',
        'projectile:s2Time': 'microtime',
        'projectile:seeksTarget': 'boolean',
        'projectile:spinSpeed': 'int',
        'projectile:cannonsPerSequence': 'int',
        'projectile:salvos': 'int',
        'projectile:cliptime': 'microtime',
        'projectile:DPS': 'float',
        # below are roles for buffs
        'buff:duration': 'microtime',
        'buff:lvl': 'int',
        'buff:msFirstProc': 'microtime',
        'buff:msPerProc': 'microtime',
        'buff:stack': 'int',
        'buff:value': 'int',
        'buff:isRefreshing': 'boolean',
        'buff:summon dieWithSummoner': 'boolean',
        'buff:summon maxProc': 'int',
        'buff:summon randomSpawnRadius': 'int',
        'buff:summon sameTeam': 'boolean',
        'buff:summon targetSummoner': 'boolean',
        'buff:summon visitorUids': 'array',
        # placeholder
        '':''
        }
    for k in keys:
        if k.endswith('mult'):
            config['stattype'][k]='percentage'
        if k.startswith('projectile:'):
            config['statrole']['abilityprojectile:'+k[11:]]='ability'+config['statrole'][k]
            config['statrole']['deathprojectile:'+k[11:]]='death'+config['statrole'][k]
            if k in config['stattype']:
                config['stattype']['abilityprojectile:'+k[11:]]=config['stattype'][k]
                config['stattype']['deathprojectile:'+k[11:]]=config['stattype'][k]
        if config['statrole'][k].startswith('attack'):
            config['statrole']['ability:'+k]='ability'+config['statrole'][k][6:]
            if k in config['stattype']:
                config['stattype']['ability:'+k]=config['stattype'][k]
    for k in config['stattype'].keys():
        type=dget(config['stattype'],k,'string')
        if type=='string':
            continue
        elif type=='int':
            continue
        elif type=='array':
            config['stathandler'][k]=display_array
        elif type=='':
            continue
        elif type=='float':
            config['stathandler'][k]=display_float
        elif type=='boolean':
            config['stathandler'][k]=display_boolean
        elif type=='time':
            config['stathandler'][k]=display_time
        elif type=='microtime':
            config['stathandler'][k]=display_microtime
        elif type=='planet':
            config['stathandler'][k]=display_planet
        elif type=='percentage':
            config['stathandler'][k]=display_percent
        elif type=='translate':
            config['stathandler'][k]=_
        elif type=='side':
            config['stathandler'][k]=display_side
        else:
            die('{} is an unknown type. Stopping'.format(type))
    # Handle automatic translations
    trans={'deathprojectile':'Death attack ','abilityprojectile':'Secondary attack ','ability':'Secondary attack '}
    for k in config['statrole'].keys():
        if k.find(':')>-1 and k not in config['stattranslation'] and k[(k.find(':')+1):] in config['stattranslation']:
            pr=''
            if k[:k.find(':')] in trans:
                pr=trans[k[:k.find(':')]]
            c=config['stattranslation'][k[(k.find(':')+1):]]
            config['stattranslation'][k]=prependlower(pr,c)
    for k in config['statrole'].keys():
        if k not in config['stattranslation']:
            if k.find(':')>-1:
                pr=''
                if k[:k.find(':')] in trans:
                    pr=trans[k[:k.find(':')]]
                config['stattranslation'][k]=prependlower(pr,camel_case_to_phrase(k[(k.find(':')+1):]))
            else:
                config['stattranslation'][k]=camel_case_to_phrase(k)


def initstatbuff(buffprefix,buffstring):
    global config
    if buffprefix in config['buffs']:
        return
    config['buffs'][buffprefix]=True
    keys=[x for x in config['statrole'].keys()]
    bp=buffprefix
    for k in keys:
        if k.startswith('buff:'):
            nk=bp+':'+k[5:]
            config['statrole'][nk]=bp+(config['statrole'][k])[4:]
            for h in ['stattype','stathandler']:
                if k in config[h]:
                    config[h][nk]=config[h][k]
            config['stattranslation'][nk]=prependlower(buffstring+' ',config['stattranslation'][k])

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

    initstat()
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
        mode='tournament,crate,unit'
        config['begin']='2012-01-01'
        config['output']='md'
        for file in os.listdir("manualdocs"):
            if file.startswith("."):
                True
            else:
                shutil.copy(os.path.join("manualdocs", file),os.path.join("docs", file))
    modes=mode.split(",")
    # Modes in one single phase
    xhelp['tables']='List all tables available in the data files, as well as the number of entries.'
    if ('tables' in modes):
        for t in data:
            print('{0};{1}'.format(t,len(data[t])))
    # Modes in one single phase
    xhelp['translate']='Searches a string ID through the SWC catalog and translates it.'
    morehelp['translate']={'':'keys to be searched  (cumulative, default: all strings)'}
    if ('translate' in modes):
        if len(elements)==0:
            elements=sorted(langdata.keys())
        for t in elements:
            string=_(t)
            print('{0};{1}'.format(t,repr(string)))
    xhelp['table']='List all keys from specific tables'
    morehelp['table']={'table':'table to search keys from (cumulative, default: all tables)','':'keys to be searched'}
    if (mode == 'table'):
        tables=config['table']
        if len(tables)==0:
            tables=sorted(data.keys())
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
            tables=sorted(data.keys())
        for table in tables:
            if (not(table) in data):
                print('Table unknown {0}'.format(config[table]))
                sys.exit(1)
            if len(elements)==0:
                xelements=sorted((data[table]).keys())
            else:
                xelements=elements
            for item in sorted(xelements):
                if (item in data[table]):
                    for t in sorted(data[table][item]):
                        print('{0};{1};{2};{3}'.format(table,item,t,data[table][item][t]))
    # Modes in two phases
    objects={}
    displayed={}
    # Acquisition phase
    ## Tournament
    xhelp['tournament']='Lists all tournaments (conflicts)'
    morehelp['tournament']={'begin':'Start date in format YYYY-MM-DD (default: current day)','end':'End date in format YYYY-MM-DD (default: 9999-12-31)','':'tournament identifier (default: all)'}
    if ('tournament' in modes):
        # do something that adds tournament objects
        for i in data['TournamentData']:
            analyse_tournament(objects,displayed,i)
    ## Crate
    xhelp['crate']='List the contents of crates'
    morehelp['crate']={'planet':'planet the crate is gained from (default: all planets, as with special value "any")','hq':'hq level (default: 5 and 10)','side':'faction (default: all factions, as with special value "any")','':'crate identifier (default: all)'}
    if ('crate' in modes):
        # do something that adds crates objects
        if len(elements)==0:
            xelements=(data['Crate']).keys()
        else:
            xelements=elements
        for i in xelements:
            analyse_crate(objects,displayed,i)
    ## Unit
    xhelp['unit']='List the statistics of units'
    morehelp['unit']={'':'unit identifier (default: all)'}
    if ('unit' in modes):
        # do something that adds tournament objects
        if len(elements)==0:
            tmpdict={}
            for u in (data['TroopData']).keys():
                uname=data['TroopData'][u]['unitID']
                if uname not in tmpdict:
                    tmpdict[uname]=1
            xelements=sorted(tmpdict.keys())
        else:
            xelements=elements
        for i in xelements:
            analyse_unit(objects,displayed,i)
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
            for crate in getdisplayed(displayed,'crate'):
                output_list_crate(out,objects,objects[crate])
        if ('md' in outputs):
            addtodisplay(displayed,'index','crate')
            output_mdheader_crate(out,objects,getdisplayed(displayed,'crate'))
            for crate in getdisplayed(displayed,'crate'):
                output_md_crate(out,objects,objects[crate])
    if ('unit' in displayed):
        if ('list' in outputs):
            output_listheader_unit(out,objects,getdisplayed(displayed,'unit'))
            for unit in getdisplayed(displayed,'unit'):
                output_list_unit(out,objects,objects[unit])
        if ('md' in outputs):
            addtodisplay(displayed,'index','unit')
            output_mdheader_unit(out,objects,getdisplayed(displayed,'unit'))
            for unit in getdisplayed(displayed,'unit'):
                output_md_unit(out,objects,objects[unit])
    if ('index' in displayed):
        id='index'
        with open("docs/{0}.md".format(id),"w") as file:
            file.write("---\ntitle: {1} ({0})\ncategory: crate\n---\n".format(id,'Main index page'))
            file.write("# {1} ({0}) — version {2}\n\n".format('index','Main index page',config['version']))
            for sid in getdisplayed(displayed,id):
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
def variantspace():
    global config
    global data
    sides=[]
    hqs=[]
    planets=[]
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
        hqs=[5,6,7,8,9,10]
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
    return (sides,hqs,planets)

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
    (sides,hqs,planets)=variantspace()
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
        HQ='HQ{0}'.format(hq)
        # Some scales are missing HQ2.
        try:
            num=data['CrateSupplyScale'][scale]['HQ{0}'.format(hq)]
        except KeyError:
            num=data['CrateSupplyScale'][scale]['HQ3']
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


def analyse_unit(objects,displayed,id):
    global data
    global config
    ob={}
    ob['levels']=[]
    ob['hq']={}
    ob['uid']=id
    ob['title']='trp_title_'+id
    ob['unknown']={}
    ob['presentation']={}
    ob['projectileTypes']={}
    ob['options']={}
    ob['roles']={}
    ob['buffs']={}
    levels=ob['levels']
    used={}
    projectiles={}
    def dobuff(bufftype,where):
        ob['options'][bufftype]=True
        lbuff=subunit[where].split(',')
        for buff in lbuff:
            bid=data['BuffData'][buff]['buffID']
            bname=bid
            if bname.startswith('buff'):
                bname=bname[4:]
            bname=camel_case_to_phrase(bname)
            ob['buffs'][bid]=bufftype
            initstatbuff(bid,bname)
            for kk in data['BuffData'][buff]:
                subunit[bid+':'+kk]=data['BuffData'][buff][kk]
            subunit[bid+':name']=bname
            if 'summon' == subunit[bid+':modifier']:
                summoned=subunit[bid+':details']
                for kk in data['SummonDetails'][summoned]:
                    subunit[bid+':summon '+kk]=data['SummonDetails'][summoned][kk]
                subunit[bid+':summon visitors']=display_unitarray(subunit,bid)
    def addprojectile(prefix,ob,subunit,data):
        damage=int(dget(data,'damage',0))
        sc=int(dget(data,'shotCount',1))
        ctime=int(dget(data,'chargeTime',0))
        cdtime=int(dget(data,'cooldownTime',0))
        stime=int(dget(data,'shotDelay',0))
        rtime=int(dget(data,'reload',0))
        gs=[ int(x) for x in data['gunSequence'].split(',') ]
        gs=sorted(gs)
        subunit[prefix+'cannonsPerSequence']=len(gs)
        salvos=(sc//len(gs))*gs[-1]
        if sc%(len(gs))>0:
            salvos+=gs[sc%(len(gs))-1]
        subunit[prefix+'salvos']=salvos
        cliptime=ctime+stime*(salvos-1)+cdtime+rtime
        subunit[prefix+'cliptime']=cliptime
        if cliptime!=0:
            subunit[prefix+'DPS']=(1000*sc*damage)/cliptime
        if prefix+'applyBuffs' in subunit:
            dobuff(prefix[:-1],prefix+'applyBuffs')

    uparray={'upgradematerials':' All.','upgradecredits':'$', 'upgradecontraband':' Con.','upgradeshards':' data fragments'}
    addtodisplay(displayed,'unit',id)
    for u in (data['TroopData']).keys():
        uname=data['TroopData'][u]['unitID']
        if uname!=id:
            continue
        subunit={}
        # subunit is a flattened version of the CSV data
        for k,v in data['TroopData'][u].items():
            subunit[k]=v
        level=int(subunit['lvl'])
        levels.append(level)
        if 'projectileType' in subunit:
            ## Do something with projectiles ; append stats with prefix 'projectile'
            ob['options']['projectile']=True
            proj=subunit['projectileType']
            pproj=data['ProjectileData'][proj]
            for kk,vv in pproj.items():
                subunit['projectile:'+kk]=vv
            addprojectile('projectile:',ob,subunit,subunit)
        if 'ability' in subunit:
            ob['options']['ability']=True
            proj=subunit['ability']
            pproj=data['HeroAbilities'][proj]
            for kk,vv in pproj.items():
                subunit['ability:'+kk]=vv
            if 'ability:selfBuff' in subunit:
                dobuff('ability','ability:selfBuff')
        if 'ability:projectileType' in subunit:
            ## Do something with projectiles ; append stats with prefix 'projectile'
            ob['options']['abilityprojectile']=True
            proj=subunit['ability:projectileType']
            pproj=data['ProjectileData'][proj]
            for kk,vv in pproj.items():
                subunit['abilityprojectile:'+kk]=vv
            fakearray={}
            for k in ['shotCount','gunSequence']:
                fakearray[k]=dget(subunit,'ability:'+k,'1')
            for k in ['damage','chargeTime','cooldownTime','shotDelay','reload']:
                fakearray[k]=dget(subunit,'ability:'+k,'0')
            addprojectile('abilityprojectile:',ob,subunit,fakearray)
        if 'deathProjectile' in subunit:
            ob['options']['death']=True
            proj=subunit['deathProjectile']
            pproj=data['ProjectileData'][proj]
            for kk,vv in pproj.items():
                subunit['deathprojectile:'+kk]=vv
            fakearray={}
            for k in ['shotCount','gunSequence']:
                fakearray[k]='1'
            fakearray['damage']=dget(subunit,'deathProjectileDamage','0')
            fakearray['chargeTime']=dget(subunit,'deathProjectileDelay','0')
            for k in ['cooldownTime','shotDelay','reload']:
                fakearray[k]='0'
            addprojectile('deathprojectile:',ob,subunit,fakearray)

        if 'spawnApplyBuffs' in subunit:
            dobuff('spawn','spawnApplyBuffs')
        # ob['hq'] is a clean version of subunit
        ob['hq'][level]={}
        a=ob['hq'][level]
        trains=[]
        targets={}
        mults={}
        upgrades=[]
        for k,v in subunit.items():
            type=dget(config['stattype'],k,'string')
            if type=='string':
                a[k]=v
            elif type=='int':
                a[k]=int(v)
            elif type=='percentage':
                a[k]=int(v)
            elif type=='array':
                a[k]=v
            elif type=='':
                continue
            elif type=='float':
                a[k]=float(v)
            elif type=='boolean':
                a[k]=v=='true'
            elif type=='time':
                a[k]=int(v)
            elif type=='microtime':
                a[k]=int(v)
            elif type=='planet':
                a[k]=v
            elif type=='translate':
                a[k]=v
            elif type=='side':
                a[k]=v
            else:
                print('{} is an unknown type. Stopping'.format(type))
                sys.exit(0)
            role=dget(config['statrole'],k,'missing')
            if role=='train':
                if a[k]>0:
                    trains.append('{0}{1}'.format(a[k],uparray['upgrade'+k.lower()]))
            elif role=='upgrade':
                if a[k]>0:
                    upgrades.append('{0}{1}'.format(a[k],uparray[k.lower()]))
            elif role.endswith('prefs'):
                if role[:-5] not in targets:
                    targets[role[:-5]]={}
                targets[role[:-5]][k]=int(a[k])
            elif role.endswith('mult'):
                if role[:-4] not in mults:
                    mults[role[:-4]]={}
                mults[role[:-4]][k]=int(a[k])
            elif role=='missing':
                die('Stat {} is unknown and has no role'.format(k),item=id)
            else:
                True
        a['sizes']='{0}x{1}'.format(a['sizex'],a['sizey'])
        if len(upgrades)==0:
            a['upgrades']='Nothing'
        else:
            a['upgrades']=', '.join(upgrades)
        if len(trains)==0:
            a['trains']='Free'
        else:
            a['trains']=', '.join(trains)
        def gettargets(targets):
            tlist=sorted(targets,key=(lambda x:'{0:04d} {1}'.format(2000-targets.get(x),config['stattranslation'][x])))
            ttlist=[]
            tmax=targets[tlist[0]]
            for t in tlist:
                if targets[t]==tmax:
                    ttlist.append('**{0} ({1})**'.format(config['stattranslation'][t],targets[t]))
                else:
                    if targets[t]<=50:
                        ttlist.append('{0} ({1})'.format(config['stattranslation'][t],targets[t]))
                    else:
                        ttlist.append('_{0} ({1})_'.format(config['stattranslation'][t],targets[t]))
            return(', '.join(ttlist))
        def getmults(targets):
            tlist=sorted(targets,key=(lambda x:'{0:04d} {1}'.format(2000-targets.get(x),config['stattranslation'][x])))
            ttlist=[]
            tmax=-1
            for t in tlist:
                if targets[t]!=tmax:
                    ttlist.append('**({1}%)**: {0}'.format(config['stattranslation'][t],targets[t]))
                    tmax=targets[t]
                else:
                    ttlist.append('{0}'.format(config['stattranslation'][t],targets[t]))
            return(', '.join(ttlist))
        a['targets']=gettargets(targets['attack'])
        if 'ability' in targets:
            a['ability:targets']=gettargets(targets['ability'])
        for k in mults.keys():
            a[k+':mults']=getmults(mults[k])
        for k in a.keys():
            ob['roles'][config['statrole'][k]]=True
    ob['firstlevel']=levels[0]
    if len(levels)==1:
        levelstring=str(levels[0])
    else:
        levelstring='{0}-{1}'.format(levels[0],levels[-1])
    for level in ob['hq'].keys():
            ob['hq'][level]['levels']=levelstring
    if id not in objects:
        objects[id]=ob


# This set of functions output objects for various modes
def output_listheader_crate(out,objects,displayed):
    out.append("There are {0} crates in the selection:".format(len(displayed)))

def output_list_crate(out,objects,item,LINKS=False):
    global config
    id=item['uid']
    title=__(item['title'])
    xout='\n# {1} ({0}){2}\n\n'.format(id,title," — version {0}".format(config['version']) if LINKS else '')
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
        thispool={}
        thispooltext={}
        for i in sorted(item['variants'][j]):
            thisvariant=''
#            thisvariant+=
            instances=item['variants'][j][i]['instances']
            lines=[]
            if (instances==0):
                lines.append('  * No items, see the fallback option below')
            for it in item['variants'][j][i]['items']:
                myit=item['variants'][j][i]['items'][it]
                lines.append('  * ({0}/{1}) {2}'.format(myit['rate'],instances,display_unitbatch(myit,LINKS)))
            thisvariant+='\n'+'\n'.join(sorted(lines))
            xhash=hashlib.sha1(thisvariant.encode('utf-8'))
            xxhash=xhash.hexdigest()
            thispooltext[xxhash]=thisvariant
            try:
                thispool[xxhash] += '/{0}'.format(i)
            except KeyError:
                thispool[xxhash]='{0}'.format(i)
        for xxhash in sorted(thispooltext):
            variants=thispool[xxhash]
            xout+='\n\n### {0}\n'.format(display_poolvariant(variants))
            xout+=thispooltext[xxhash]
        for i in sorted(item['variantsdefaults'][j]):
            xout+='\n\n### Fallback{0}\n'.format(display_poolvariant(i,False))
            myit=item['variantsdefaults'][j][i]
            xout+='\n  * {0}'.format(display_unitbatch(myit,LINKS))
    out[len(out)-1]+=xout

def output_mdheader_crate(out,objects,displayed):
    with open("docs/crate.md","w") as file:
        file.write("---\ntitle: Index of crates\n---\n")
        file.write("# Crates — version {0}\n\n".format(config['version']))
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
        file.write("# Conflicts — version {0}\n\n".format(config['version']))
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


def output_listheader_unit(out,objects,displayed):
    out.append("There are {0} units in the selection:".format(len(displayed)))

def output_list_unit(out,objects,item,LINKS=False):
    global config
    id=item['uid']
    title=__(item['title'])
    levels=sorted(item['levels'])
    allkeys=config['statrole']
    xout='\n# {1} ({0}){2}\n\n'.format(id,title," — version {0}".format(config['version']) if LINKS else '')
    if LINKS:
        xout+=("You can read an [explanation  of the various unit stats](unitexplained.md).\n\n")
    tosee=[x for x in item['roles'].keys()]
    def remove(tosee,x):
        if x in tosee:
            tosee.remove(x)
    remove(tosee,'')
    def datadump(somelist):
        return display_leveldata(item['hq'],levels,somelist,config['stattranslation'],config['stathandler'])
    firstlevel=levels[0]
    xout+='## Main stats\n\n'
    xout+='### Unit stats\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='basic']))
    remove(tosee,'basic')
    xout+='### Training stats\n\n'
    req=0
    trainlist=sorted([x for x in allkeys if allkeys[x]=='xtrain'])
    remove(tosee,'train')
    remove(tosee,'xtrain')
    for l in levels:
        if 'requirements' in item['hq'][l]:
            ll=len(item['hq'][l]['requirements'])
        else:
            ll=0
        if ll>req:
            req=ll
    for ll in range(0,req):
        r='requirement'+str(ll)
        trainlist.append(r)
        config['stattranslation'][r]='Building '+str(ll)
        if req==1:
            config['stattranslation'][r]='Building'
        for l in levels:
            if 'requirements' in item['hq'][l]:
                a=item['hq'][l]['requirements']
            else:
                a=[]
            if ll<len(a):
                item['hq'][l][r]=display_building(a[ll],LINKS)
            else:
                item['hq'][l][r]='None'
    xout+=datadump(trainlist)
    xout+='### Upgrading stats\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='xupgrade']))
    remove(tosee,'upgrade')
    remove(tosee,'xupgrade')
    xout+='### Movement stats\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='move']))
    remove(tosee,'move')
    attacknames=[]
    def display_modifiers(item,s):
        xout=''
        notfound=True
        for k in item['buffs']:
            if item['buffs'][k]==s:
                notfound=False
                xout+='#### Modifier "{}"\n\n'.format(item['hq'][firstlevel][k+':name'])
                xout+=datadump(sorted([x for x in allkeys if allkeys[x]==k+'basic']))
                xout+=datadump(sorted([x for x in allkeys if allkeys[x]==k+'details']))
                remove(tosee,k+'basic')
                remove(tosee,k+'details')
        return(xout)
    for l in sorted(levels):
        if 'projectile:name' in item['hq'][l]:
            n=item['hq'][l]['projectile:name']
            if n not in attacknames:
                attacknames.append(n)
    if ('spawn' in item['options']):
        xout+='### Modifiers\n\n'
        xout+=display_modifiers(item,'spawn')
    xout+='## Main attack{0}{1}\n\n'.format(' : ' if len(attacknames)>0 else '',' / '.join(attacknames))
    xout+='### Targeting\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='attackmove']))
    remove(tosee,'attackmove')
    remove(tosee,'attackprefs')
    xout+='### Shooting\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='attackstats']))
    remove(tosee,'attackstats')
    if 'projectile' in item['options']:
        xout+='### Projectile\n\n'
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='projectilebasic']+['dps']))
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='projectilemisc']))
        remove(tosee,'projectilebasic')
        remove(tosee,'projectilemult')
        remove(tosee,'projectilemisc')
        xout+=display_modifiers(item,'projectile')
    if 'ability' in item['options']:
        attacknames=[]
        for l in sorted(levels):
            if 'abilityprojectile:name' in item['hq'][l]:
                n=item['hq'][l]['abilityprojectile:name']
                if n not in attacknames:
                    attacknames.append(n)
        xout+='## Secondary attack{0}{1}\n\n'.format(' : ' if len(attacknames)>0 else '',' / '.join(attacknames))
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='abilityonly']))
        xout+='### Targeting\n\n'
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='abilitymove']))
        xout+='### Shooting\n\n'
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='abilitystats']))
        xout+=display_modifiers(item,'ability')
    remove(tosee,'abilityonly')
    remove(tosee,'abilitymove')
    remove(tosee,'abilitystats')
    remove(tosee,'abilityprefs')
    if 'abilityprojectile' in item['options']:
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='abilityprojectilebasic']))
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='abilityprojectilemisc']))
        xout+=display_modifiers(item,'abilityprojectile')
    remove(tosee,'abilityprojectilebasic')
    remove(tosee,'abilityprojectilemult')
    remove(tosee,'abilityprojectilemisc')
    if 'death' in item['options']:
        attacknames=[]
        for l in sorted(levels):
            if 'deathprojectile:name' in item['hq'][l]:
                n=item['hq'][l]['deathprojectile:name']
                if n not in attacknames:
                    attacknames.append(n)
        xout+='## Death attack{0}{1}\n\n'.format(' : ' if len(attacknames)>0 else '',' / '.join(attacknames))
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='deathbasic']))
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='deathprojectilebasic']))
        xout+=datadump(sorted([x for x in allkeys if allkeys[x]=='deathprojectilemisc']))
    remove(tosee,'deathbasic')
    remove(tosee,'deathprojectilebasic')
    remove(tosee,'deathprojectilemult')
    remove(tosee,'deathprojectilemisc')
    # All other stats
    def removebysuffix(tosee,s):
        x=[y for y in tosee]
        for rem in tosee:
            if rem.endswith(s) or rem==s:
                remove(x,rem)
        return x
    tosee=removebysuffix(tosee,'nodisplay')
    xout+='## Internal stats\n\nThese stats internal to the system link different parts of data together.\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x].endswith('internal')],key=config['stattranslation'].get))
    tosee=removebysuffix(tosee,'internal')
    xout+='## Presentation stats\n\nThese are all sorts of user interface settings, that should not interfere with gameplay.\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x].endswith('presentation')],key=config['stattranslation'].get))
    tosee=removebysuffix(tosee,'presentation')
    xout+='## Uninterpreted stats\n\nSeriously, we don\'t really know what to do with these.\n\n'
    xout+=datadump(sorted([x for x in allkeys if allkeys[x].endswith('unknown')],key=config['stattranslation'].get))
    tosee=removebysuffix(tosee,'unknown')
    if len(tosee)>0:
        xout+='I could not show the following roles, because I was not programmed to : '+', '.join(tosee)+'\n'
    out[len(out)-1]+=xout
    return

def output_mdheader_unit(out,objects,displayed):
    with open("docs/unit.md","w") as file:
        file.write("---\ntitle: Index of units\n---\n")
        file.write("# Units — version {0}\n\n".format(config['version']))
        file.write("The site contains an [explanation of the unit stats](unitexplained.md).\n\n")
        pfd={True:'Buildable units',False:'Other units'}
        for pf in [True, False]:
            file.write("## {0}\n\n".format(pfd[pf]))
            sides={}
            for unit in displayed:
                item=objects[unit]
                firstlevel=item['firstlevel']
                if item['hq'][firstlevel]['playerFacing']==pf:
                    sides[item['hq'][firstlevel]['faction']]=1
            for side in sorted(sides):
                file.write("### {0}\n\n".format(display_side(side)))
                for unit in displayed:
                    item=objects[unit]
                    firstlevel=item['firstlevel']
                    if item['hq'][firstlevel]['playerFacing']==pf:
                        if item['hq'][firstlevel]['faction']==side:
                            id=item['uid']
                            title=__(item['title'])
                            file.write("  * [{1} ({0})]({0}.html)\n".format(id,title))
                file.write("\n")

def output_md_unit(out,objects,item):
    id=item['uid']
    title=__(item['title'])
    with open("docs/{0}.md".format(id),"w") as file:
        file.write("---\ntitle: {1} ({0})\ncategory: unit\n---\n".format(id,title))
        lout=['']
        output_list_unit(lout,objects,item,True)
        file.write(lout[0])


# This set of functions take an Id and return the adequate string for it

def display_planet(planetId):
    return _('planet_name_'+planetId)

def display_float(xx):
    x=float(xx)
    if x%1<0.001:
        return(str(int(x)))
    else:
        return '%.3f' % x
    return _('planet_name_'+planetId)

def display_boolean(x):
    if x:
        return 'Yes'
    return 'No'

def display_array(x):
    return ', '.join(map(str,x))

def display_side(side):
    if (side=='empire'):
        return 'Empire'
    if (side=='rebel'):
        return 'Rebellion'
    if (side=='smuggler'):
        return 'Independant units'
    if (side=='tusken'):
        return 'Tusken Raiders'
    if (side=='neutral'):
        return 'Other units'
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

def display_time(s,micro=False):
    t=[]
    s=int(s)
    if (s<0):
        return 'permanent'
    hsecs=0
    if micro:
        hsecs=s%1000
        s=int((s-hsecs)/1000)
    sec=s%60
    s=int((s-sec)/60)
    min=s%60
    s=int((s-min)/60)
    hour=s%24
    s=int((s-hour)/24)
    day=s%7
    s=int((s-day)/7)
    out=''
    if (s>0):
        out+='{0}w'.format(s)
    if (day>0):
        out+='{0}d'.format(day)
    if (hour>0):
        out+='{0}h'.format(hour)
    if (min>0):
        out+='{0}m'.format(min)
    if (sec>0 or hsecs>0):
        if micro:
            if sec==0:
                out+='{0}ms'.format(hsecs)
            else:
                if hsecs>100:
                    out+='{0}.{1}s'.format(sec,hsecs)
                elif hsecs>10:
                    out+='{0}.0{1}s'.format(sec,hsecs)
                elif hsecs>0:
                    out+='{0}.00{1}s'.format(sec,hsecs)
                else:
                    out+='{0}s'.format(sec)
        else:
            out+='{0}s'.format(sec)
    if (out==''):
        return('0s')
    return(out)

def display_microtime(s):
    return display_time(s,True)

def display_percent(s):
    return '{}%'.format(s)

def display_poolvariant(variants,cap=True):
    variantsarray=variants.split('/')
    def describehq(space,levels,cap):
        s2=':'.join([str(l) for l in sorted(space)])
        if levels==s2:
            return ''
        else:
            xlevels=[]
            for l in levels.split(':'):
                xlevels.append(int(l))
            xlevels.sort()
        pairs=[]
        num=len(xlevels)
        while len(xlevels)>0:
            start=xlevels[0]
            current=start
            while (current in xlevels):
                xlevels.remove(current)
                current+=1
            stop=current-1
            if stop==start:
                pairs.append('{0}'.format(start))
            else:
                pairs.append('{0}-{1}'.format(start,stop))
        if pairs[0]=='2-10':
            return ''
        if cap:
            sentence='For HQ'
        else:
            sentence=' for HQ'
        if (num>1):
            sentence+=' levels '
        else:
            sentence+=' level '
        sentence+=', '.join(pairs)
        return sentence

    def describeplanet(space,planets,cap):
        if planets==':'.join(space):
            return ''
        planetsarr=planets.split(':')
        if planetsarr[0]=='any':
            return ''
        if cap:
            sentence='On '
        else:
            sentence=' on '
        planetnames=[]
        for p in planetsarr:
            planetnames.append(display_planet(p))
        return sentence+' or '.join(sorted(planetnames))

    def describefaction(space,factions,cap):
        if factions==':'.join(space):
            return ''
        prefix='' if cap else ' '
        factionsarr=factions.split(':')
        far=[display_side(f) for f in factionsarr]
        return prefix+(' or '.join(far))

    (sides,hqs,planets)=variantspace()
    poolbysidebyplanet={}
    for s in variantsarray:
        (side,hq,planet)=s.split(',')
        if side in poolbysidebyplanet:
            if planet in poolbysidebyplanet[side]:
                pass
            else:
                poolbysidebyplanet[side][planet]={}
        else:
            poolbysidebyplanet[side]={}
            poolbysidebyplanet[side][planet]={}
        if hq=='any':
            for h in hqs:
                hh='{0}'.format(h)
                poolbysidebyplanet[side][planet][hh]=1
        else:
                poolbysidebyplanet[side][planet][hq]=1
    variantsarray=[]
    for side in poolbysidebyplanet.keys():
        for planet in poolbysidebyplanet[side].keys():
            thqs=sorted(poolbysidebyplanet[side][planet].keys(),key=int)
            variantsarray.append('{2},{1},{0}'.format(planet,':'.join(thqs),side))
    poolbysidebyhq={}
    for s in variantsarray:
        (side,hq,planet)=s.split(',')
        if side in poolbysidebyhq:
            if hq in poolbysidebyhq[side]:
                pass
            else:
                poolbysidebyhq[side][hq]={}
        else:
            poolbysidebyhq[side]={}
            poolbysidebyhq[side][hq]={}
        if planet=='any':
            for p in planets:
                poolbysidebyhq[side][hq][p]=1
        else:
                poolbysidebyhq[side][hq][planet]=1
    variantsarray=[]
    for side in poolbysidebyhq.keys():
        for planet in poolbysidebyhq[side].keys():
            pl=sorted(poolbysidebyhq[side][hq].keys())
            variantsarray.append('{2},{1},{0}'.format(':'.join(pl),hq,side))
    poolbyplanetbyhq={}
    for s in variantsarray:
        (side,hq,planet)=s.split(',')
        if planet in poolbyplanetbyhq:
            if hq in poolbyplanetbyhq[planet]:
                pass
            else:
                poolbyplanetbyhq[planet][hq]={}
        else:
            poolbyplanetbyhq[planet]={}
            poolbyplanetbyhq[planet][hq]={}
        if side=='any':
            for si in sides:
                poolbyplanetbyhq[planet][hq][si]=1
        else:
                poolbyplanetbyhq[planet][hq][side]=1
    variantsarray=[]
    for planet in poolbyplanetbyhq.keys():
        for hq in poolbyplanetbyhq[planet].keys():
            si=sorted(poolbyplanetbyhq[planet][hq].keys())
            variantsarray.append('{2},{1},{0}'.format(planet,hq,':'.join(si)))
    pieces=[]
    ocap=cap
    for s in variantsarray:
        final=''
        (side,hq,planet)=s.split(',')
        f=describefaction(sides,side,cap)
        if len(f)>0:
            cap=False
        final=f
        f=describeplanet(planets,planet,cap)
        if len(f)>0:
            cap=False
        final+=f
        f=describehq(hqs,hq,cap)
        if len(f)>0:
            cap=False
        final+=f
        pieces.append(final)
    final=' or '.join(pieces)
    if final=='':
        if cap:
            final='Always'
    return final

def display_building(i,link):
    global data
    global config
    r=data['BuildingData'][i]['buildingID']
    level=data['BuildingData'][i]['lvl']
    if link:
        r='[{0} {2}]({1}.html)'.format(_('bld_title_'+r),r,level)
    else:
        r='{0} {2}'.format(_('bld_title_'+r),r,level)
    return r

def display_unitarray(item,bid,link=True):
    if item[bid+':summon visitorType']=='specialAttack':
        True
    return ''
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

def display_leveldata(data,levels,keys,titles,funcs,LINKS=False):
    notfound='(not found)'
    commonvalues=[]
    notfoundvalues=[]
    variablevalues=[]
    display={}
    firstlevel=levels[0]
    for key in keys:
        if key in funcs:
            func=funcs[key]
        else:
            func=str
        display[key]={}
        identical=True
        dataitem=dget(data[firstlevel],key,notfound)
        for level in levels:
            v=dget(data[level],key,notfound)
            if key in data[level]:
                display[key][level]=func(v)
            else:
                display[key][level]=v
            if v!=dataitem:
                identical=False
        if identical:
            if (dataitem==notfound):
                notfoundvalues.append(key)
            else:
                commonvalues.append(key)
        else:
            variablevalues.append(key)
    output=''
    for key in commonvalues:
        t=key
        if key in titles:
            t=titles[key]
        output+='  * {0}: {1}\n'.format(t,display[key][firstlevel])
    if len(notfoundvalues)>0:
        True
    #    output+='  * _Not found: {0}_\n'.format(', '.join(sorted(map(lambda x:titles[x],notfoundvalues))))
    # for key in notfoundvalues:
    #     t=key
    #     if key in titles:
    #         t=titles[key]
    #     output+='  * {0}: _{1}_\n'.format(t,display[key][firstlevel])
    old=''
    displevel={}
    newlevs=[]
    newdisp={}
    if len(variablevalues)>0:
        for key in variablevalues:
            newdisp[key]={}
        for level in levels:
            newlevel='{}'.format(level)
            new=''
            for key in variablevalues:
                new+='ABCDEFGHIJKL'+display[key][level]
            if new==old:
                oldlev=newlevs[-1]
                newlev=oldlev+', '+newlevel
                for key in variablevalues:
                    newdisp[key][newlev]=newdisp[key][oldlev]
                    del newdisp[key][oldlev]
                newlevs[-1]=newlev
            else:
                newlev=newlevel
                newlevs.append(newlevel)
            for key in variablevalues:
                newdisp[key][newlev]=display[key][level]
            old=new
        levels=newlevs
        display=newdisp
        if len(levels)>10:
            sublevels=[]
            while len(levels)>10:
                sublevels.append(levels[0:10])
                levels=levels[10:]
            sublevels.append(levels)
        else:
            sublevels=[levels]
        for levels in sublevels:
            width={}
            width['label']=5
            for level in levels:
                width[level]=len(level)
                for key in variablevalues:
                    w=len(display[key][level])
                    if w>width[level]:
                        width[level]=w
            for key in variablevalues:
                t=key
                if key in titles:
                    t=titles[key]
                w=len(t)
                if w>width['label']:
                    width['label']=w
            if len(output)>0:
                output+='\n'
            if len(variablevalues)>0:
                line='|'
                line+='{message: <{width}}|'.format(message='Level',width=width['label'])
                for level in levels:
                    line+='{message: <{width}}|'.format(message=str(level),width=width[level])
                line+='\n|'
                line+=('-'*width['label'])+'|'
                for level in levels:
                    line+=('-'*width[level])
                    line+='|'
                line+='\n'
                for key in variablevalues:
                    t=key
                    if key in titles:
                        t=titles[key]
                    line+='|'
                    line+='{message: <{width}}|'.format(message=t,width=width['label'])
                    for level in levels:
                        line+='{message: <{width}}|'.format(message=display[key][level],width=width[level])
                    line+='\n'
                output+=line+'\n'
    output+='\n'
    return(output)

def display_leveldataunique(data,levels,key,funcs,LINKS=False):
    firstlevel=levels[0]
    if key in funcs:
        func=funcs[key]
    else:
        func=str
    display={}
    identical=True
    dataitem=dget(data[firstlevel],key,notfound)
    for level in levels:
        v=dget(data[level],key,notfound)
        if key in data[level]:
            display[level]=func(v)
        else:
            display[level]=v
        if v!=dataitem:
            identical=False
    if identical:
        if (dataitem==notfound):
            return None
        else:
            return display[firstlevel]
    else:
        return ''



if __name__ == "__main__":
    main(sys.argv)
