# OSG
# ⌨ >= ⚔
# Prussian Red v1.1
# Python 3
# This program is inspired by Ed Snowden's book Permanent Record towards the end of chapter 16
# "It's basically an I Ching stochastic procedure that randomly picks words from two columns."
# Prussian Red is a Project Name Generator

import random

# intro
print("Executing...")
print("""
  _____                    _               _____          _
 |  __ \                  (_)             |  __ \        | |
 | |__) | __ _   _ ___ ___ _  __ _ _ __   | |__) |___  __| |
 |  ___/ '__| | | / __/ __| |/ _` | '_ \  |  _  // _ \/ _` |
 | |   | |  | |_| \__ \__ \ | (_| | | | | | | \ \  __/ (_| |
 |_|   |_|   \__,_|___/___/_|\__,_|_| |_| |_|  \_\___|\__,_|
""")


print("""
                                       /
                                    ,**/(/*
                                    *#//#/(
                                   *@@@@@(@,                       &
                 .@@@@@@   @.     ,,.**@@@@@@       @%  @@@@@@@
         #@@@@@@@@@%*,.@@@@@/&& %     (.(#%@@@.     @@@@@(***@@@@@(@@@@,
      # @@@.#@@/@@@@*@     @            @@@(@*@      % @  @@*@@@ @@@ @@@  @
        /@@.@@&@@@@@(@@#    *  @@   .  @@@@@@@   @@  #   @@@*@@@@.@@@@@@
     @@@   / @@@@,@@*@@@     /       @@@@@@(*@           @@*@((@@@@&@   @@@@
        @  @@*@@@@@@@@.@@@@@        @@@@@@@*        ,@@@@#*@@@@@@@@,@@ (@
        @@&@@@*/@@@@@@@@*%@@@@   &@@@@@@@@@@@@@   @@@@@*(@@@@@*%@@ @@(@@#
      @@@@( # @ @*(@@%@@##@***@@@@@@@@@@@(@/@@@@@@,.*@@,@@ @@@#@%@@* @/@@@%
    @@@@   .@@%@(@/@@@@@@@@@@@@@%@@@@*@#/@//@@@@@@@#@@@@@@@%(@@@@@*@ @  @%(@
         @ @@%/(&&@@@&@ @(@/@@,@@@@@@@#/(*@@@@@@@@@@@@ @@%@@##@ @@@%@@*@     .
        & @*@@*%&@@@@@@@(@@@ #@@*  ,@*@@@@*@/@ @ @@@@@@@@* @@.@@  @@&@@ @
     /@  @ @@@&@@,@@@..@,@@@ /@@/ *@@,@@@@&@@@ @ @@@ &@@@@  @@%@@  @@/@@  @
    @  /@.@@@( @,/@%  @@@@@*,/@*@ @@@@@@@.@@@@,  @@. @@@@@/@%@@@@%. @@,@@   &
       @ @@@  (@@@@ @ @#@@@ &   ,@@@@@@@ @@@@@@@@    ,@@*@@  @@@.@ @*@@/@@
      @@@@  %(@@@*%  #@@@@    *@@@@@//(@@@@@@@@@@&    %@@&@ @ @@ @@ @ &@ @@
     @%@@  @ @ @@/.@ @@#@@   @@@@@@. (@&@,(  @@@@@@@   @@@@    @%%@  (  @@@%
   /@@@   @  @,@@&*  @@@@ @/.**(@&(   .@@@%   @@@,, @,,/@&@  @ @(#%@     @@@@
         @  @@@#/ *& @@@   ****(@@ *  @#@@& *   @@,...   @@@###%#@(@%  @
      @    (@@@  @,#*(   **/    @.,%. @.@@  .@ ,     ,,/ .*#(#(((/#%@   &
      &   ,@@%  %,**#/**#          ,* @&@@@ & #         /*/#(*((%*#@@@    (
          @@,  @ @%#*(*        @,@  ..&@@(#    @*@        /**//(/   @@@
        @.   &@    @*&   @@@@@   @  %,,(@*@@  @@   @*@*@          @    @%
            (          / @ (@&@@@@@/ & #@@@&  @@%@@*@ &,@          .
                      @@@@  @@@@@@@@@@ @@@@@@@%@@@@@% @@@@
                     .@@     ,@@@@@   #@@@@  #@@@@@   @  @@@
                           @@@.  @  @,(@@*@@  @   @@(%
                               @@@@@   @@@  &@@@@.
                                   ,(#@@@ @ .
                                     @ (@
                                       *,
""")

# Part 1 collect user input categories
input("Press enter to continue:")

choicelist = """1) Random
2) Aquatic Animals
3) Birds
4) Bladed Weapons
5) Celestial
6) Colors
7) Felines
8) Geographic & Landforms
9) Greek & Roman Myths
10) Greek Alphabet
11) IC Codenames
12) Materials
13) Mythical Creatures
14) Places
15) Planets
16) Prefixes
17) Science
18) Shapes
19) Snakes
20) Toxins
21) Trees
22) Venomous or Biting Animals
23) Weather & Atmosphere
>"""

#input 0 is prefix category
print("""
Select a prefix:
0) No prefix""")
input0 = int(input(choicelist))

#While loop to reject invalid user input
while input0<=-1 or input0>=24:
    print("\nInvalid input")
    print("Try again")
    print("""
Select a prefix:
0) No prefix""")
    input0 = int(input(choicelist))

# input 1 is base word category
print("\nSelect a base-word:")
input1 = int(input(choicelist))

while input1<=-1 or input1>=24:
    print("\nInvalid input")
    print("Try again")
    print("\nSelect a base-word:")
    input1 = int(input(choicelist))

# input 2 is suffix category
print("""
Select a suffix:
0) No suffix""")
input2 = int(input(choicelist))

while input2<=-1 or input2>=24:
    print("\nInvalid input")
    print("Try again")
    print("""
Select a suffix:
0) No suffix""")
    input2 = int(input(choicelist))

# Init category lists

aquatic_animals = ['Alligator', 'Barracuda', 'Crocodile', 'Gator', 'Great White',
'Hammerhead', 'Jaws', 'Lionfish', 'Mako', 'Moray', 'Orca', 'Piranha', 'Shark',
'Stingray']

birds = ['Albatross', 'Bald Eagle','Blackhawk','Blue Jay','Chukar','Condor','Crane',
'Dove','Eagle','Falcon','Goose (Golden Goose)','Grouse','Hawk','Heron',
'Hornbill','Hummingbird','Lark','Mallard','Oriole','Osprey',
'Owl','Parrot','Penguin','Peregrine','Pelican','Pheasant','Quail','Raptor',
'Raven','Robin','Sandpiper','Seagull','Sparrow','Stork','Thunderbird',
'Toucan','Vulture','Waterfowl','Woodpecker','Wren']

bladed_weapons = ['Axe','Battle Axe','Bayonet','Blade','Crossbow','Dagger'
,'Excalibur','Halberd','Harpoon','Hatchet','Machete','Saber','Samurai','Scimitar'
,'Scythe','Skewer','Stiletto','Spear','Sword','Tomahawk','Gladius']

celestial = ['Andromeda','Aquila','Cassiopeia','Celestial','Cepheus','Cygnus','Comet',
'Delphinus','Drako','Eclipse','Galactic','Lunar','Lyra','Meteor','Nova','Orbit(al)',
'Orion','Perseus','Portal','Satellite','Serpens','Solar','Space','Star','Stellar','Supernova',
'Triangulum','Universe']

colors = ['Aero','Amber','Azure','Beaver','Black','Blue','Bronze','Brown','Cadet',
'Camel','Charcoal','Crystal','Cyan','Ebony','Drab','Emerald','Fallow','Flame','Flax',
'Frostbite','Green','Gunmetal','Iceberg','Independence','Ivory','Jet',
'Liberty','Lava','Midnight','Mint','Mystic','Onyx','Opal','Orange','Oxblood','Red','Scarlet','Shadow',
'Snow','Sunglow','Sunray','Sunset','Volt','White']

felines = ['Badger','Black Cat','Bobcat','Caracal','Cheetah','Cougar','Jaguar',
'Leopard','Lion','Lynx','Mountain Lion','Ocelot','Panther','Puma','Siamese',
'Serval','Tiger','Wolverine']

geographic_landforms = ['Abyss','Arch','Atoll','Bay','Beach','Beach','Bluff','Cape'
,'Cavern','Chasm','Cove','Crater','Desert','Den','Dune','Horizon','Mountain'
,'Plain','Summit','Valley']

greek__roman_myths = ['Ajax','Apollo','Ares','Artemis','Athena','Cyclopes',
'Hercules','Hermes','Iris','Medusa','Minotaur','Nemesis','Neptune','Pandora',
'Perseus','Poseidon','Talos','Triton','Zeus']

greek_alphabet = ['Alpha','Beta''Gamma','Delta','Epsilon','Zeta','Theta','Iota',
'Kappa','Lamda','Omikron','Pi','Rho','Sigma','Tau','Ypsilon','Phi','Khi','Psi',
'Omega',]

IC_codenames = ['Acorn','Aegis','Agile','Apex','Argonaut','Artichoke','Azorian',
'Birch','Blackjack','Blackshield','Blockbuster','Brimstone','Capital','Cartwheel',
'Chopstick','Circle','Colossus','Eastwind','Forbidden','Foxhound','Genesis',
'Gusto','Hawkeye','Invader','Ironside','Keyhole','Keystone','Lancelot','Magnum',
'Monarch','Nomad','Octagon','Orange','Outlaw','Patriot','Phalanx','Phoenix','Prism','Rainbow',
'Razor','Revelation','Rover','Shakedown','Shockwave','Shooter','Square','Stargate',
'Steamroller','Sunray','Vector','Volley','Washtub']

materials = ['Chrome','Cobalt','Copper','Gold','Helium','Hydrogen','Iridium',
'Iron','Krypton','Lead','Lithium','Mercury','Neon','Nickel','Nitrogen','Oxygen',
'Platinum','Radon','Silicon','Silver','Tin','Titanium','Tungsten','Quartz',
'Wood','Xenon']

mythical_creatures = ['Basilisk','Bigfoot','Medusa','Kraken','Siren','Dragon',
'Matador','Pegasus','Yeti','Thunderbird']

places = ['Aberdeen','Altis','Arctic','Armageddon','Aurora','Belgium','Blue Ridge',
'Burmuda','Cape Town','Chernarus','Chernobyl','Cheyenne','Erie','Everest','Exeter',
'Falcon Lake','Groom Lake','Huron','Harcourt','Labyrinth','Langley','Loch Ness','London',
'Manhattan','Mclean','Michigan','Moscow','Nuremberg','Olympus','Ontario','Oreokastro',
'Passchendaele','Pangaea','Petra','Pripyat','Raven Rock','Roswell','Savannah','Sawtooth',
'Scotland','Siberia','Stratis','Superior','Sydney','Tanoa','Texas','Thule','Transylvania','Valhalla',
'Vostok','Warrenton','Washington','Zion']

planets = ['Earth','Jupiter','Mars','Mercury','Neptune','Saturn','Venus']

prefixes = ['Atto','Exa','Femto','Giant','Giga','Kilo','Meta','Micro','Nano','Peta','Pico','Tera'
'Tiny','Titanic']

science = ['Acid','Acid Rain','Alkali','Alkaloid','Anomaly','Catalyst','Core','Electron',
'Fluorescent','Fusion','Gravity','Inherent','Kinetic','Laser','Light','Mechanical',
'Metric','Neutron','Optical','Particle','Radian','Radiation','Reactor','Skeptic','Sonar',
'Spectrum','Thermal']

shapes = ['Astroid','Circle','Digon','Heptagon','Hexagon','Lune','Pentagon'
'Prism','Sphere','Spiral','Triangle']

snakes = ['Anaconda','Boa','Cobra','Copperhead','Cottonmouth','Garter','Kingsnake'
'Mamba','Python','Rattler','Sidewinder','Taipan','Viper']

toxins = ['Arsine','Chlorine','Cyanide','Lewisite','Phosgene','Ricin','Sarin']

# “The creation of a thousand forests is in one acorn” ― Ralph Waldo Emerson
trees = ['Ash','Cypress','Oak','Willow']

venomous_or_biting_animals = ['Abispa','Andrena','Black Widow','Cataglyphis'
'Centipede','Cephalotes','Formica','Hornet','Jellyfish','Scorpion','Tarantula',
'Wasp','Yellowjacket']

weather_atmosphere = ['Aurora','Avalanche','Blizzard','Cyclone','Dewdrop',
'Downpour','Duststorm','Fogbank','Freeze','Frost','Gust','Hurricane','Ice Storm',
'Jet Stream','Lightning','Maelstrom','Mist','Monsoon','Rainbow','Raindrop',
'Sand Storm','Seabreeze','Snowflake','Stratosphere','Storm','Sunrise','Sunset',
'Tornado','Thunder','Thunderbolt','Thunderstorm','Tropical Storm','Twilight',
'Twister','Typhoon','Updraft','Vortex','Waterspout','Whirlwind','Wind Chill']

# List of lists
big_list = list(zip(aquatic_animals, birds,bladed_weapons,celestial,colors,
felines,geographic_landforms,greek__roman_myths,greek_alphabet,IC_codenames,
materials,mythical_creatures,places,planets,prefixes,science,shapes,snakes,
toxins,trees,venomous_or_biting_animals,weather_atmosphere))

#Part 2 Assign variables via random number generation.

if input0 == 0:
     print("\n")

elif input0 == 1:
    output0 = random.choice(big_list)
    output0 = random.choice(output0)
    print(output0)

elif input0 == 2:
    output0 = random.choice(aquatic_animals)
    print(output0)

elif input0 == 3:
    output0 = random.choice(birds)
    print(output0)

elif input0 == 4:
    output0 = random.choice(bladed_weapons)
    print(output0)

elif input0 == 5:
    output0 = random.choice(celestial)
    print(output0)

elif input0 == 6:
    output0 = random.choice(colors)
    print(output0)

elif input0 == 7:
    output0 = random.choice(felines)
    print(output0)

elif input0 == 8:
    output0 = random.choice(geographic_landforms)
    print(output0)

elif input0 == 9:
    output0 = random.choice(greek__roman_myths)
    print(output0)

elif input0 == 10:
    output0 = random.choice(greek_alphabet)
    print(output0)

elif input0 == 11:
    output0 = random.choice(IC_codenames)
    print(output0)

elif input0 == 12:
    output0 = random.choice(materials)
    print(output0)

elif input0 == 13:
    output0 = random.choice(mythical_creatures)
    print(output0)

elif input0 == 14:
    output0 = random.choice(places)
    print(output0)

elif input0 == 15:
    output0 = random.choice(planets)
    print(output0)

elif input0 == 16:
    output0 = random.choice(prefixes)
    print(output0)

elif input0 == 17:
    output0 = random.choice(science)
    print(output0)

elif input0 == 18:
    output0 = random.choice(shapes)
    print(output0)

elif input0 == 19:
    output0 = random.choice(snakes)
    print(output0)

elif input0 == 20:
    output0 = random.choice(birds)
    print(output0)

elif input0 == 21:
    output0 = random.choice(trees)
    print(output0)

elif input0 == 22:
    output0 = random.choice(venomous_or_biting_animals)
    print(output0)

elif input0 == 23:
    output0 = random.choice(weather_atmosphere)
    print(output0)

#Start baseword
if input1 == 0:
    print("\n")

elif input1 == 1:
    output1 = random.choice(big_list)
    output1 = random.choice(output1)
    print(output1)

elif input1 == 2:
    output1 = random.choice(aquatic_animals)
    print(output1)

elif input1 == 3:
    output1 = random.choice(birds)
    print(output1)

elif input1 == 4:
    output1 = random.choice(bladed_weapons)
    print(output1)

elif input1 == 5:
    output1 = random.choice(celestial)
    print(output1)

elif input1 == 6:
    output1 = random.choice(colors)
    print(output1)

elif input1 == 7:
    output1 = random.choice(felines)
    print(output1)

elif input1 == 8:
    output1 = random.choice(geographic_landforms)
    print(output1)

elif input1 == 9:
    output1 = random.choice(greek__roman_myths)
    print(output1)

elif input1 == 10:
    output1 = random.choice(greek_alphabet)
    print(output1)

elif input1 == 11:
    output1 = random.choice(IC_codenames)
    print(output1)

elif input1 == 12:
    output1 = random.choice(materials)
    print(output1)

elif input1 == 13:
    output1 = random.choice(mythical_creatures)
    print(output1)

elif input1 == 14:
    output1 = random.choice(places)
    print(output1)

elif input1 == 15:
    output1 = random.choice(planets)
    print(output1)

elif input1 == 16:
    output1 = random.choice(prefixes)
    print(output1)

elif input1 == 17:
    output1 = random.choice(science)
    print(output1)

elif input1 == 18:
    output1 = random.choice(shapes)
    print(output1)

elif input1 == 19:
    output1 = random.choice(snakes)
    print(output1)

elif input1 == 20:
    output1 = random.choice(toxins)
    print(output1)

elif input1 == 21:
    output1 = random.choice(trees)
    print(output1)

elif input1 == 22:
    output1 = random.choice(venomous_or_biting_animals)
    print(output1)

elif input1 == 23:
    output1 = random.choice(weather_atmosphere)
    print(output1)

#start suffix

if input2 == 0:
    print("\n")

elif input2 == 1:
    output2 = random.choice(big_list)
    output2 = random.choice(output2)
    print(output2)

elif input2 == 2:
    output2 = random.choice(aquatic_animals)
    print(output2)

elif input2 == 3:
    output2 = random.choice(birds)
    print(output2)

elif input2 == 4:
    output2 = random.choice(bladed_weapons)
    print(output2)

elif input2 == 5:
    output2 = random.choice(celestial)
    print(output2)

elif input2 == 6:
    output2 = random.choice(colors)
    print(output2)

elif input2 == 7:
    output2 = random.choice(felines)
    print(output2)

elif input2 == 8:
    output2 = random.choice(geographic_landforms)
    print(output2)

elif input2 == 9:
    output2 = random.choice(greek__roman_myths)
    print(output2)

elif input2 == 10:
    output2 = random.choice(greek_alphabet)
    print(output2)

elif input2 == 11:
    output2 = random.choice(IC_codenames)
    print(output2)

elif input2 == 12:
    output2 = random.choice(materials)
    print(output2)

elif input2 == 13:
    output2 = random.choice(mythical_creatures)
    print(output2)

elif input2 == 14:
    output2 = random.choice(places)
    print(output2)

elif input2 == 15:
    output2 = random.choice(planets)
    print(output2)

elif input2 == 16:
    output2 = random.choice(prefixes)
    print(output2)

elif input2 == 17:
    output2 = random.choice(science)
    print(output2)

elif input2 == 18:
    output2 = random.choice(shapes)
    print(output2)

elif input2 == 19:
    output2 = random.choice(snakes)
    print(output2)

elif input2 == 20:
    output2 = random.choice(toxins)
    print(output2)

elif input2 == 21:
    output2 = random.choice(trees)
    print(output2)

elif input2 == 22:
    output2 = random.choice(venomous_or_biting_animals)
    print(output2)

elif input2 == 23:
    output2 = random.choice(weather_atmosphere)
    print(output2)
