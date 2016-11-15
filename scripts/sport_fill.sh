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
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Baseball',$sportsTypeID,'sport_img/baseball.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Cricket',$sportsTypeID,'sport_img/cricket.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Rugby',$sportsTypeID,'sport_img/rugby.png');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Soccer',$sportsTypeID,'sport_img/soccer.png');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Fitness'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Boxing',$sportsTypeID,'sport_img/boxing.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Climbing',$sportsTypeID,'sport_img/climbing.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Crossfit',$sportsTypeID,'sport_img/crossfit.jpeg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Gymnastics',$sportsTypeID,'sport_img/gymnastics.jpg');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Games / Entertainment'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Bowling',$sportsTypeID,'sport_img/bowling.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Chess',$sportsTypeID,'sport_img/chess.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Dart',$sportsTypeID,'sport_img/dart.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Poker',$sportsTypeID,'sport_img/poker.jpg');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Outdoor Activities'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Airsoft',$sportsTypeID,'sport_img/airsoft.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Archery',$sportsTypeID,'sport_img/archery.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Camping',$sportsTypeID,'sport_img/camping.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Hiking',$sportsTypeID,'sport_img/hiking.jpg');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Action Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Basejump',$sportsTypeID,'sport_img/basejump.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('BMX',$sportsTypeID,'sport_img/bmx.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Motorbike',$sportsTypeID,'sport_img/motorbike.png');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Skating',$sportsTypeID,'sport_img/skating.jpg');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Playground / Gym'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('3D Dodgeball',$sportsTypeID,'sport_img/3d_dodgeball.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Handball',$sportsTypeID,'sport_img/handball.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Over the time',$sportsTypeID,'sport_img/game_over.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Quidditch',$sportsTypeID,'sport_img/quidditch.jpg');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Water Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Swimming',$sportsTypeID,'sport_img/swimming.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Diving',$sportsTypeID,'sport_img/diving.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Rowing',$sportsTypeID,'sport_img/rowing.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Surfing',$sportsTypeID,'sport_img/surfing.jpg');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Grass / Feild Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Beach Tennis',$sportsTypeID,'sport_img/beach_tennis.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Gold',$sportsTypeID,'sport_img/gold.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Polo',$sportsTypeID,'sport_img/polo.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Tennis',$sportsTypeID,'sport_img/tennis.jpg');" 

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Winter Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Skiing',$sportsTypeID,'sport_img/skiing.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Snowboarding',$sportsTypeID,'sport_img/snowboarding.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('SnowsHoeing',$sportsTypeID,'sport_img/snowshoeing.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Snowmobiling',$sportsTypeID,'sport_img/snowmobiling.jpg');"

sportsTypeID=`sqlite3 $db "Select id from Core_sportstype where categoryName='Olympic Sports'"`
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Badminton',$sportsTypeID,'sport_img/badminton.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Curling',$sportsTypeID,'sport_img/curling.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Fencing',$sportsTypeID,'sport_img/fencing.jpg');"
sqlite3 $db "Insert into Core_sports (sportName,sportType_id,sportImage) values ('Judo',$sportsTypeID,'sport_img/judo.jpg');"
