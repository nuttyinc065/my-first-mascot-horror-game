# Initializes scoreboards, bossbar, and persistent state for The Anomlys mode
scoreboard objectives add anomlys_state dummy
scoreboard objectives add anomlys_night dummy
scoreboard objectives add anomlys_corruption dummy
scoreboard objectives add anomlys_alerts dummy

bossbar remove anomlys:corruption
bossbar add anomlys:corruption "Nutty'Inc Corruption"
bossbar set anomlys:corruption max 100
bossbar set anomlys:corruption color purple
bossbar set anomlys:corruption style notched_10

function anomlys:reset
