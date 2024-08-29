# build_files.sh
echo "Building project packages......."
pip3 install -r requirements.txt

echo "Migrating databases......."
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

echo "Collecting static files......"
python3 manage.py collectstatic --no-input --clear

# echo "creating a superuser......."
# python3 manage.py createsuperuserunique --no-input