# Prussian Red 0.1v Using Python 3.8.6
# This program is inspired by Ed Snowden's book Permanent Record towards the end of chapter 16
# "It's basically an I Ching stochastic procedure that randomly picks words from two columns."
# Prussian Red is a Project Name Generator
import random
import linecache

#Part 1 intro
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


input("Press enter to continue:")

input0 = int(input("""

Select a prefix:
0) No prefix
1) Random
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
>"""))

input1 = int(input("""
Select a base-word:

1) Random
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
>"""))

input2 = int(input("""
Select a suffix:
0) No suffix
1) Random
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
>"""))

# If wordlist1.txt is changed, then all blank and category title lines have got be added to this list,
# Otherwise, you have a codword of "IC codewords" or other category title.
nogonumbers = [1,2,17,18,19,60,61,62,83,84,85,114,115,116,161,162,163,182,183,184,205,206,207,227,227,229,250
 ,251,252,305,306,307,334,335,337,347,348,349,404,405,406,414,415,416,431,432,4033,460,461,462,474,
 475,476,490,491,492,500,501,502,507,508,509,523,524,525]

#Part 2 Assign variables via random number generation.
if input0 == 0:
    number0 = random.randrange(3,565)

elif input0 == 1:
    number0 = random.randrange(3, 565)
    while number0 == nogonumbers:
        number0 = random.randrange(3, 565)
    else:
        print(linecache.getline('wordlist1.txt', number0))

elif input0 == 2:
    number0 = random.randrange(3,16)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 3:
    number0 = random.randrange(20,59)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 4:
    number0 = random.randrange(63,82)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 5:
    number0 = random.randrange(86,113)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 6:
    number0 = random.randrange(117,160)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 7:
    number0 = random.randrange(164,181)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 8:
    number0 = random.randrange(185,204)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 9:
    number0 = random.randrange(208,226)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 10:
    number0 = random.randrange(230,249)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 11:
    number0 = random.randrange(253,304)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 12:
    number0 = random.randrange(308,333)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 13:
    number0 = random.randrange(337,346)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 14:
    number0 = random.randrange(350,403)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 15:
    number0 = random.randrange(407,413)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 16:
    number0 = random.randrange(417,430)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 17:
    number0 = random.randrange(434,459)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 18:
    number0 = random.randrange(463,473)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 19:
    number0 = random.randrange(477,489)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 20:
    number0 = random.randrange(493,499)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 21:
    number0 = random.randrange(503,506)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 22:
    number0 = random.randrange(510,522)
    print(linecache.getline('wordlist1.txt', number0))

elif input0 == 23:
    number0 = random.randrange(526,565)
    print(linecache.getline('wordlist1.txt', number0))

#Start baseword
if input1 == 0:
    number1 = random.randrange(3,565)

elif input1 == 1:
    number1 = random.randrange(3,565)
    while number1==nogonumbers:
        number1 =random.randrange(3,565)
    else:
        print(linecache.getline('wordlist1.txt', number1))

elif input1 == 2:
    number1 = random.randrange(3,16)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 3:
    number1 = random.randrange(20,59)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 4:
    number1 = random.randrange(63,82)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 5:
    number1 = random.randrange(86,113)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 6:
    number1 = random.randrange(117,160)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 7:
    number1 = random.randrange(164,181)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 8:
    number1 = random.randrange(185,204)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 9:
    number1 = random.randrange(208,226)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 10:
    number1 = random.randrange(230,249)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 11:
    number1 = random.randrange(253,304)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 12:
    number1 = random.randrange(308,333)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 13:
    number1 = random.randrange(337,346)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 14:
    number1 = random.randrange(350,403)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 15:
    number1 = random.randrange(407,413)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 16:
    number1 = random.randrange(417,430)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 17:
    number1 = random.randrange(434,459)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 18:
    number1 = random.randrange(463,473)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 19:
    number1 = random.randrange(477,489)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 20:
    number1 = random.randrange(493,499)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 21:
    number1 = random.randrange(503,506)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 22:
    number1 = random.randrange(510,522)
    print(linecache.getline('wordlist1.txt', number1))

elif input1 == 23:
    number1 = random.randrange(526,565)
    print(linecache.getline('wordlist1.txt', number1))

#start suffix

if input2 == 0:
    number2 = random.randrange(3,565)

elif input2 == 1:
    number2 = random.randrange(3, 565)
    while number2 == nogonumbers:
        number2 = random.randrange(3, 565)
    else:
        print(linecache.getline('wordlist1.txt', number2))

elif input2 == 2:
    number2 = random.randrange(3,16)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 3:
    number2 = random.randrange(20,59)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 4:
    number2 = random.randrange(63,82)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 5:
    number2 = random.randrange(86,113)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 6:
    number2 = random.randrange(117,160)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 7:
    number2 = random.randrange(164,181)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 8:
    number2 = random.randrange(185,204)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 9:
    number2 = random.randrange(208,226)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 10:
    number2 = random.randrange(230,249)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 11:
    number2 = random.randrange(253,304)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 12:
    number2 = random.randrange(308,333)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 13:
    number2 = random.randrange(337,346)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 14:
    number2 = random.randrange(350,403)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 15:
    number2 = random.randrange(407,413)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 16:
    number2 = random.randrange(417,430)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 17:
    number2 = random.randrange(434,459)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 18:
    number2 = random.randrange(463,473)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 19:
    number2 = random.randrange(477,489)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 20:
    number2 = random.randrange(493,499)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 21:
    number2 = random.randrange(503,506)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 22:
    number2 = random.randrange(510,522)
    print(linecache.getline('wordlist1.txt', number2))

elif input2 == 23:
    number2 = random.randrange(526,565)
    print(linecache.getline('wordlist1.txt', number2))
