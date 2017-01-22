from pyo import Server, Input, Print, Yin

# Ensure jack server is running
# jackd -r -d alsa -r 44100 -d hw:2,0
# jackd -d alsa -r 44100 -C hw:2,0 -P hw:1,0

s = Server(audio='jack')
s.boot()

i = Input().out()

s.start()

pitch = Yin(i, tolerance=0.2, winsize=8192)
#p = Print(pitch, method=0, interval=0.2, message='RMS')

#while True:
#    pass
