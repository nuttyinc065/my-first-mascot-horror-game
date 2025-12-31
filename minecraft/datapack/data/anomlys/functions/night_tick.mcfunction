# Scheduled once per second while the mode is running
execute unless score global anomlys_state matches 1 run return 1

# Increase corruption, clamp at 100, and update bossbar
scoreboard players add global anomlys_corruption 1
execute if score global anomlys_corruption matches 101.. run scoreboard players set global anomlys_corruption 100
execute store result bossbar anomlys:corruption value run scoreboard players get global anomlys_corruption

# Alert milestones to push intensity forward
execute if score global anomlys_corruption matches 35.. if score global anomlys_alerts matches ..0 run title @a actionbar {"text":"The mascot's costume smells like ozone...","color":"light_purple"}
execute if score global anomlys_corruption matches 35.. if score global anomlys_alerts matches ..0 run scoreboard players set global anomlys_alerts 1

execute if score global anomlys_corruption matches 70.. if score global anomlys_alerts matches ..1 run playsound minecraft:entity.warden.ambient master @a ~ ~ ~ 0.8 1.2
execute if score global anomlys_corruption matches 70.. if score global anomlys_alerts matches ..1 run scoreboard players set global anomlys_alerts 2

# Advance night when corruption maxes out
execute if score global anomlys_corruption matches 100 run function anomlys:advance_night

# Reschedule this loop
schedule function anomlys:night_tick 1s replace
