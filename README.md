# MeteorDetect

(WORK IN PROGRESS!!)

Algorithm idea to improve meteor detection comes from from Bart Declercq.
This is a simple python version of this algo.

Algo from Bart ( in dutch, need to cleanup this readme):

Om de meteoren makkelijker zichtbaar te maken doe ik de volgende stappen:
Voor verwerking van beeld "B" uit een reeks A, B, C, D,...

1) Mediaansom van A+B+C
2) Mediaansom uit (1) aftrekken van beeld B
3) Gamma van beeld uit (2) aftrekken van beeld B

## Usage (also in Dutch for now):

Stappen om te reproduceren:
1. Python virtual env opzetten en activeren
```
python3 -m venv meteoor_env/
source meteoor_env/bin activate
```
2. Nodige packages instaleren
```
pip install numpy opencv-python
```
3. Extract png's van Bart's gif
```
convert -coalesce 52261037249_fc554da70e_o.gif out%05d.png
```
4. Process aparte frames
```
python median_parallel.py out*.png
```
5. Maak gif van processed frames
```
convert -delay 0 -loop 0 out_median*.png proc.gif
```

