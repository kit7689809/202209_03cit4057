import WavSteg as en

WAVE_FILE = "doc/music.wav"
SECRET_BMP = "doc/secret.bmp"
OUTPUT_WAVE_FILE = "doc/musichidden.wav"

def main():
    en.hide_data(
        WAVE_FILE,
        SECRET_BMP,
        OUTPUT_WAVE_FILE,
        1 )

if __name__ == "__main__":
    main()