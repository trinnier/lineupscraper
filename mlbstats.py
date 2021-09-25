import statsapi
import pandas as pd
import time

df = pd.read_csv('FanDuel.csv')
df = df[df['Starter'] == 1]
df_Pitchers = df[df['Roster Position'] == 'P']
df_Pitchers = df_Pitchers[['Nickname']]
df_Batters = df[df['Roster Position'] != 'P']
df_Batters = df_Batters[['Nickname']]
print(df_Pitchers.shape)
print(df_Batters.shape)

bats = df_Batters['Nickname'].fillna('######').tolist()
pitchers = df_Pitchers['Nickname'].fillna('######').tolist()

pitchoutput = {}
batoutput = {}

def Extract_Stats(players, g):

   batting  = {'Name': [], 'id': [],'gamesPlayed': [], 'groundOuts': [], 'airOuts': [], 'runs': [], 'doubles': [], 'triples': [], 'homeRuns': [],
                'strikeOuts': [], 'baseOnBalls': [], 'intentionalWalks': [], 'hits': [], 'hitByPitch': [], 'avg': [], 'atBats': [], 'obp': [], 'slg': [],
                'ops': [], 'caughtStealing': [], 'stolenBases': [], 'stolenBasePercentage': [], 'groundIntoDoublePlay': [], 'numberOfPitches': [], 'plateAppearances': [],
                'totalBases': [], 'rbi': [], 'leftOnBase': [], 'sacBunts': [], 'sacFlies': [], 'babip': [], 'groundOutsToAirouts': [], 'catchersInterference': [], 'atBatsPerHomeRun': []}

   pitch = {'Name': [], 'id': [], 'gamesPlayed': [], 'gamesStarted': [], 'groundOuts': [], 'airOuts': [], 'runs': [], 'doubles': [], 'triples': [], 'homeRuns': [], 'strikeOuts': [], 'baseOnBalls': [],
            'intentionalWalks': [], 'hits': [], 'hitByPitch': [], 'avg': [], 'atBats': [], 'obp': [], 'slg': [], 'ops': [], 'caughtStealing': [], 'stolenBases': [],
            'stolenBasePercentage': [], 'groundIntoDoublePlay': [], 'numberOfPitches': [], 'era': [], 'inningsPitched': [], 'wins': [], 'losses': [], 'saves': [],
            'saveOpportunities': [], 'holds': [], 'blownSaves': [], 'earnedRuns': [], 'whip': [], 'battersFaced': [], 'outs': [], 'gamesPitched': [], 'completeGames': [],
            'shutouts': [], 'strikes': [], 'strikePercentage': [], 'hitBatsmen': [], 'balks': [], 'wildPitches': [], 'pickoffs': [], 'totalBases': [], 'groundOutsToAirouts': [],
            'winPercentage': [], 'pitchesPerInning': [], 'gamesFinished': [], 'strikeoutWalkRatio': [], 'strikeoutsPer9Inn': [], 'walksPer9Inn': [],
            'hitsPer9Inn': [], 'runsScoredPer9': [],'homeRunsPer9': [], 'inheritedRunners': [], 'inheritedRunnersScored': [], 'catchersInterference': [],
            'sacBunts': [], 'sacFlies': []}

   for p in players:
     time.sleep(5)
     try:
        player = statsapi.lookup_player(p)
        id = player[0]['id']
        name =  player[0]['fullName']
     except:
        print(p)
     try:
        player_detail = statsapi.player_stat_data(id, group=g, type='season')
        if g == 'hitting':
           batting['Name'].append(name)
        else:
           pitch['Name'].append(name)
        for i in player_detail['stats'][0]['stats']:
           if g == 'hitting':
              batting[i].append(player_detail['stats'][0]['stats'][i])
           else:
              pitch[i].append(player_detail['stats'][0]['stats'][i])
     except:
        print(p)
   if g == 'hitting':
      return batting
   else:
      return pitch

pitchoutput = Extract_Stats(pitchers, 'pitching')
dfpitch = pd.DataFrame.from_dict(pitchoutput, orient='index')
dfpitch = dfpitch.transpose()
dfpitch.to_csv('pitch.csv')

#batoutput = Extract_Stats(bats, 'hitting')
#dfbat= pd.DataFrame.from_dict(batoutput, orient='index')
#dfbat = dfbat.transpose()
#dfbat.to_csv('batters.csv')

dfpitch['StrikeoutRate'] = (dfpitch['strikeOuts'] / dfpitch['battersFaced']) * 100
dfpitch = dfpitch[['Name', 'era', 'battersFaced', 'strikeOuts', 'strikeoutsPer9Inn',
                   'walksPer9Inn','hitsPer9Inn','runsScoredPer9', 'homeRunsPer9', 'whip', 'StrikeoutRate']]

dffinal = pd.DataFrame()
dfout = pd.merge(df, dfpitch, how='left', left_on = 'Nickname', right_on = 'Name')
dfp = dfout[dfout['Position'] == 'P']
dfb = dfout[dfout['Position'] != 'P']
dfp1 = dfp[['Team_x','Nickname','era']]
print(dfb.columns)

dff = pd.merge(dfb, dfp1, how='left', left_on = 'Opponent', right_on = 'Team_x')
dfp = dfp[['Player ID + Player Name','Id','Position','First Name','Nickname','Last Name','FPPG','Played','Salary','Game','Team_x','Opponent','Injury Indicator',
           'Injury Details','Tier','Probable Pitcher','Batting Order','Roster Position','Starter','StrikeoutRate']]
dfp.rename(columns={'Team_x': 'Team', 'StrikeoutRate': 'Pitcher'}, inplace=True)
dfTeam = pd.read_csv('TeamTotals.csv')
dfp = pd.merge(dfp, dfTeam, how='left', left_on = 'Team', right_on = 'Team')
dfp['Park'] = ''
dffinal = dffinal.append(dfp)

dff = dff[['Player ID + Player Name','Id','Position','First Name','Nickname_x','Last Name','FPPG','Played','Salary','Game','Team_x_x','Opponent','Injury Indicator',
           'Injury Details','Tier','Probable Pitcher','Batting Order','Roster Position', 'Starter', 'era_y']]


dff.rename(columns={'Nickname_x': 'Nickname', 'Team_x_x': 'Team', 'era_y': 'Pitcher'}, inplace = True)
dff.to_csv('bat.csv')
dff = pd.merge(dff, dfTeam, how='left', left_on = 'Team', right_on = 'Team')



dffinal = dffinal.append(dff,ignore_index=True)
dffinal['Weight'] = ''
dffinal['FPG'] = dffinal['FPPG']
dffinal = dffinal[['Player ID + Player Name','Id','Position','First Name','Nickname','Last Name','FPPG','Played','Salary','Game','Team','Opponent','Injury Indicator',
           'Injury Details','Tier','Probable Pitcher','Batting Order','Roster Position', 'Starter', 'Pitcher', 'Park', 'Runs', 'Weight', 'FPG']]
dffinal.to_csv('FD.csv')











