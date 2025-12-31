# Resets state and hides corruption UI until the mode is started
scoreboard players set global anomlys_state 0
scoreboard players set global anomlys_night 0
scoreboard players set global anomlys_corruption 0
scoreboard players set global anomlys_alerts 0

bossbar set anomlys:corruption value 0
bossbar set anomlys:corruption visible false

# Clear lingering effects
team remove AnomlysPlayers
team add AnomlysPlayers "Anomlys Crew"
team join AnomlysPlayers @a

say [Anomlys] Mode reset. Run /function anomlys:start to enter the facility.
