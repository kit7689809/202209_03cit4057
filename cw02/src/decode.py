import WavSteg as en

WAVE_FILE = "doc/music.wav"
SECRET_BMP = "doc/secret.bmp"
OUTPUT_WAVE_FILE = "doc/musichidden.wav"
RECOVERD_BMP = "doc/recover.bmp"

def main():
    en.recover_data(
        OUTPUT_WAVE_FILE,
        RECOVERD_BMP,
        1,
        460000 )

if __name__ == "__main__":
    main()