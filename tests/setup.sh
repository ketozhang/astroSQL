pip uninstall -y astrosql
pip install ../
python main_test.py

read -n1 -p "Uninstall and clean astrosql? ([y]/n)" clean
case $clean in
    n|N) echo ;;
#    *) pip uninstall -y astrosql ;;
esac
