if [[ "$OSTYPE" == "darwin"* ]]; then
    python3 -m venv .venv
    . .venv/Scripts/activate
    pip install -r requirements.txt

elif [[ "$OSTYPE" == "msys" ]]; then
    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

else 
    echo "Incompatible OS"
fi