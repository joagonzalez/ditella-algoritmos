#  ______               _                            _                  _                 _                  _ _                       
# |  ____|             | |                          | |                | |          /\   | |                (_) |                      
# | |__ _   _ _ __   __| | __ _ _ __ ___   ___ _ __ | |_ ___  ___    __| | ___     /  \  | | __ _  ___  _ __ _| |_ _ __ ___   ___  ___ 
# |  __| | | | '_ \ / _` |/ _` | '_ ` _ \ / _ \ '_ \| __/ _ \/ __|  / _` |/ _ \   / /\ \ | |/ _` |/ _ \| '__| | __| '_ ` _ \ / _ \/ __|
# | |  | |_| | | | | (_| | (_| | | | | | |  __/ | | | || (_) \__ \ | (_| |  __/  / ____ \| | (_| | (_) | |  | | |_| | | | | | (_) \__ \
# |_|   \__,_|_| |_|\__,_|\__,_|_| |_| |_|\___|_| |_|\__\___/|___/  \__,_|\___| /_/    \_\_|\__, |\___/|_|  |_|\__|_| |_| |_|\___/|___/
#                                                                                            __/ |                                     
#                                                                                           |___/                                 
# Agustin Alba Chicar
# Joaquin Gonzalez
# sh tp1_tests.sh <filename>
#!/bin/bash
echo "Comando a Ejecutar por línea de comando           |      Resultado impreso por pantalla"
echo "----------------------------------------------------------------------------------"
echo -n "python3 $1 esPrimo 2                          | " 
python3 $1 esPrimo 2
echo -n "python3 $1 esPrimo 6                          | " 
python3 $1 esPrimo 6 
echo -n "python3 $1 iesimoPrimo 1                      | " 
python3 $1 iesimoPrimo 1
echo -n "python3 $1 iesimoPrimo 5                      | " 
python3 $1 iesimoPrimo 5  
echo -n "python3 $1 cantidadPrimosMenoresOIguales 6    | " 
python3 $1 cantidadPrimosMenoresOIguales 6
echo -n "python3 $1 cantidadPrimosMenoresOIguales 7    | " 
python3 $1 cantidadPrimosMenoresOIguales 7
echo -n "python3 $1 cantidadDivisoresPrimos 6          | " 
python3 $1 cantidadDivisoresPrimos 6
echo -n "python3 $1 cantidadDivisoresPrimos 7          | " 
python3 $1 cantidadDivisoresPrimos 7
echo -n "python3 $1 iesimoDivisorPrimo 10 1            | " 
python3 $1 iesimoDivisorPrimo 10 1
echo -n "python3 $1 iesimoDivisorPrimo 10 2            | " 
python3 $1 iesimoDivisorPrimo 10 2
echo -n "python3 $1 iesimoDivisorPrimo 10 3            | " 
python3 $1 iesimoDivisorPrimo 10 3
echo -n "python3 $1 sumaPrimerosPrimos 1               | " 
python3 $1 sumaPrimerosPrimos 1
echo -n "python3 $1 sumaPrimerosPrimos 3               | " 
python3 $1 sumaPrimerosPrimos 3
echo -n "python3 $1 sumaPrimerosPrimos 5               | " 
python3 $1 sumaPrimerosPrimos 5
