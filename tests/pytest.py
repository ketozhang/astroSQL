import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parents[1]))
from astrosql.astrosql import AstroSQL

def test_check_config_exists():
    assert (Path.home()/'.astrosql'/'config.yml').exists()