#!/bin/sh

db=$1
echo "This script would populate tables in $db ."
echo "Deleting core_sportstype"
sqlite3 $db "DELETE FROM Core_sportstype;"
sqlite3 $db "delete from sqlite_sequence where name='Core_sportstype';"
echo "Inserting into core_sportstype"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Team Sports');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Fitness');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Games / Entertainment');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Outdoor Activities');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Action Sports');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Playground / Gym');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Water Sports');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Grass / Feild Sports');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Winter Sports');"
sqlite3 $db "Insert into Core_sportstype (categoryName) values ('Olympic Sports');"

echo "Deleting Core_sports"
sqlite3 $db "DELETE FROM Core_sports;"
sqlite3 $db "delete from sqlite_sequence where name='Core_sports';"
echo "Inserting into Core_sports"
sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Team Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Baseball',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Cricket',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Rugby',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Soccer',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Fitness'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Boxing',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Climbing',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Crossfit',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Gymnastics',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Games / Entertainment'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Bowling',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Chess',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Dart',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Poker',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Outdoor Activities'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Airsoft',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Archery',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Camping',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Hiking',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Action Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Basejump',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('BMX',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Motorbike',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Skating',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Playground / Gym'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('3D Dodgeball',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Handball',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Over the time',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Quidditch',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Water Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Swimming',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Diving',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Rowing',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Surfing',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Grass / Feild Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Beach Tennis',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Gold',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Polo',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Tennis',$sportsTypeID);" 

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Winter Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Skiing',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Snowboarding',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('SnowsHoeing',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Snowmobiling',$sportsTypeID);"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Olympic Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Badminton',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Curling',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Fencing',$sportsTypeID);"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id) values ('Judo',$sportsTypeID);"
