if python3.12 --version > /dev/null; then
  python=python3.12
elif python3 --version; then
  python=python3
elif python --version; then
  python=python
fi

if ! $python test.py --locals -v --durations 0; then
  $python test.py -v
fi