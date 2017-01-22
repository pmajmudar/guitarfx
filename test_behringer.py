from pyo import Server, Input, Freeverb, Record, Disto, Delay, Chorus

# Ensure jack server is running
# jackd -r -d alsa -r 44100 -d hw:2,0
# jackd -r -d alsa -r 48000 -p 512 -n 3 -d hw:2,0
# jackd -d alsa -r 44100 -C hw:2,0 -P hw:1,0

s = Server(audio='jack')
s.boot()

i = Input().out()

# s.start()

reverb = Freeverb(i, size=0.8, damp=1, bal=1, mul=.8).out()

# dist = Disto(i, drive=0.95, slope=0.5).out()

#delay = Delay(i, delay=0.5, feedback=0.5).out()

# chorus = Chorus(i, depth=2, feedback=0.5, bal=0.5).out()

s.start()
while True:
    pass
# rec = (reverb, '/home/prash/pyo_test_rev.wav')
# s.recstart()
# s.recstop()
