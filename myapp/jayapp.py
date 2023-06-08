import fire

def hello(name="World"):
  return "Greetings from %s (updated)!" % name

if __name__ == '__main__':
  fire.Fire(hello)
