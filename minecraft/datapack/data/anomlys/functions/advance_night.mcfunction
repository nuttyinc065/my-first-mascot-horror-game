# Escalates the scenario into the next night and re-seeds corruption
scoreboard players add global anomlys_night 1
scoreboard players set global anomlys_corruption 10
scoreboard players set global anomlys_alerts 0
execute store result bossbar anomlys:corruption value run scoreboard players get global anomlys_corruption

playsound minecraft:entity.vex.charge master @a ~ ~ ~ 1 1.2
execute as @a at @s run summon zombie ~ ~1 ~ {IsBaby:0b,CustomName:'{"text":"Nutty Mascot"}',PersistenceRequired:1b,ArmorItems:[{},{},{},{id:"minecraft:carved_pumpkin",Count:1b}]}

title @a subtitle {"text":"Night ","color":"gray","bold":false,"extra":[{"score":{"name":"global","objective":"anomlys_night"}}]}
title @a title {"text":"Corruption rising","color":"dark_purple","bold":true}
say [Anomlys] Night has advanced. The mascot is restless.
