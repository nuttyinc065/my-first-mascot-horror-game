# Passive per-tick hooks (nothing heavy to avoid lag); corruption loop is scheduled separately
execute if score global anomlys_state matches 1 run function anomlys:ambient
