# Starts The Anomlys mode and schedules the corruption loop
scoreboard players set global anomlys_state 1
scoreboard players set global anomlys_night 1
scoreboard players set global anomlys_corruption 5

bossbar set anomlys:corruption value 5
bossbar set anomlys:corruption visible true
bossbar set anomlys:corruption players @a

title @a subtitle {"text":"Nutty'Inc facility breach"}
title @a title {"text":"The Anomlys","color":"dark_purple","bold":true}
playsound minecraft:block.portal.trigger master @a ~ ~ ~ 1 0

# Create a lobby ring of particles around players to suggest the facility staging area
particle minecraft:portal ~ ~1 ~ 0.5 0.2 0.5 0.05 30 force @a

# Kick off the corruption loop and night timer
schedule function anomlys:night_tick 1s replace
say [Anomlys] Night 1 has begun. Survive as the mascot hunts.
