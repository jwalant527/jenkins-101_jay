import fire

def hello(name="World"):
  return "Hello from %s (updated)!" % name

if __name__ == '__main__':
  fire.Fire(hello)
