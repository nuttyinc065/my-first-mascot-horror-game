# Light ambient effects when corruption is rising
execute if score global anomlys_corruption matches 25.. run effect give @a[m=0] minecraft:darkness 1 0 true
execute if score global anomlys_corruption matches 40.. run playsound minecraft:ambient.cave master @a ~ ~ ~ 0.8 0.8
execute if score global anomlys_corruption matches 65.. run particle minecraft:soul ~ ~1 ~ 0.4 0.6 0.4 0.02 12 force @a
