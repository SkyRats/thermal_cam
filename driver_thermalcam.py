'''
import i2c

mlx = i2c.grove_mxl90640()
mlx.refresh_rate = i2c.seeed_mlx9064x.RefreshRate.REFRESH_8_HZ
try:
     
          frame = [0]*768
          #frame = [0]*192
          mlx.getFrame(frame)
     except ValueError:
          continue
'''






import i2c as seeed_mlx9064x
import time
CHIP_TYPE = 'MLX90640'
def main():
    if CHIP_TYPE == 'MLX90641':
        mlx = seeed_mlx9064x.grove_mxl90641()
        frame = [0] * 192
    elif CHIP_TYPE == 'MLX90640':
        mlx = seeed_mlx9064x.grove_mxl90640()
        frame = [0] * 768       
    time.sleep(1)
    mlx.getFrame(frame)
    print(frame)
''' 
    while True:
        start = time.time()
        try:
            mlx.getFrame(frame)
        except ValueError:
            continue
        print(frame)
        end = time.time()
        print("The time: %f"%(end - start))
'''
if __name__  == '__main__':
    main()
