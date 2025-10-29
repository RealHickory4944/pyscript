import pyscript as ps

def test_say():
  assert say("text") is print("text")

def test_log():
  assert log("text") is print("text")
