import sys


def test_greeting(capsys):
    if "sple_physics" in sys.modules:
        del sys.modules["sple_physics"]

    import sple_physics  # imports the lib to check if the test_greeting is working

    dummy = sple_physics.__name__  # dummy usage to satisfy ruff

    captured = capsys.readouterr()
    assert captured.out == "Good morning and all that\n"
    print(dummy)  # useless print to avoid editor warnings.
