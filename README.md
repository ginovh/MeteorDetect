# MeteorDetect

(WORK IN PROGRESS!!)

## Intro

Algorithm idea to improve meteor detection comes from from Bart Declercq.
This is a simple python version of this algo.

Algo from Bart ( in dutch, need to cleanup this readme):

Om de meteoren makkelijker zichtbaar te maken doe ik de volgende stappen:
Voor verwerking van beeld "B" uit een reeks A, B, C, D,...

1) Mediaansom van A+B+C
2) Mediaansom uit (1) aftrekken van beeld B
3) Gamma van beeld uit (2) aftrekken van beeld B

## Example ( Example data from Bart Declercq )

 <table>
  <tr>
    <th>Original recorded data (11 frames)</th>
    <th>After applying the above algorithm</th>
  </tr>
  <tr>
    <td><img src="testdata/52261037249_fc554da70e_o.gif"  width="400" height="400" /></td>
    <td><img src="testdata/52259782297_39a5f8e20d_o.gif"  width="400" height="400" /><</td>
  </tr>
</table> 

## Usage :

1. Setup and activate Python virtual env
```
python3 -m venv meteoor_env/
source meteoor_env/bin activate
```
2. Install required packages
```
pip install numpy opencv-python
```
3. Extract png's from Bart's gif (this was only needed for me to get testdata, skip if you have frames already)
```
convert -coalesce 52261037249_fc554da70e_o.gif out%05d.png
```
4. Process frames
```
python median_parallel.py out*.png
```
5. (Optional) Create animated gif from processed frames
```
convert -delay 0 -loop 0 out_median*.png proc.gif
```

