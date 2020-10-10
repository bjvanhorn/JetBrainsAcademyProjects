# put your python code here
hours_one = int(input())
minutes_one = int(input())
seconds_one = int(input())

hours_two = int(input())
minutes_two = int(input())
seconds_two = int(input())

print(hours_two * 60 * 60
      + minutes_two * 60
      + seconds_two
      - hours_one * 60 * 60
      - minutes_one * 60
      - seconds_one)
