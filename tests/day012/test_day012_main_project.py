import pytest

from day012.day012_main_project import (
    EASY_LEVEL_TURNS,
    HARD_LEVEL_TURNS,
    check_guess,
    parse_difficulty,
    parse_guess,
    play,
)


def fake_input(monkeypatch, answers):
    """Make input() return each of answers in turn, ignoring the prompt."""
    replies = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(replies))


@pytest.mark.parametrize(
    ("guess", "expected"),
    [(30, "low"), (70, "high"), (50, "correct")],
)
def test_check_guess(guess, expected):
    assert check_guess(guess, 50) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("easy", EASY_LEVEL_TURNS),
        ("hard", HARD_LEVEL_TURNS),
        ("  HARD ", HARD_LEVEL_TURNS),
        ("medium", None),
        ("", None),
    ],
)
def test_parse_difficulty(text, expected):
    assert parse_difficulty(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("50", 50),
        ("1", 1),
        ("100", 100),
        (" 7 ", 7),
        ("0", None),
        ("101", None),
        ("abc", None),
        ("3.5", None),
        ("", None),
    ],
)
def test_parse_guess(text, expected):
    assert parse_guess(text) == expected


def test_play_win(monkeypatch, capsys):
    fake_input(monkeypatch, ["25", "75", "50"])
    assert play(answer=50, turns=5) is True
    out = capsys.readouterr().out
    assert "Too low." in out
    assert "Too high." in out
    assert "You got it! The answer was 50." in out


def test_play_lose(monkeypatch, capsys):
    fake_input(monkeypatch, ["1", "2"])
    assert play(answer=50, turns=2) is False
    out = capsys.readouterr().out
    assert "You have 1 attempt remaining" in out
    assert "You've run out of guesses. The answer was 50." in out


def test_invalid_guess_does_not_use_a_turn(monkeypatch, capsys):
    fake_input(monkeypatch, ["abc", "500", "50"])
    assert play(answer=50, turns=1) is True
    assert "Please enter a whole number" in capsys.readouterr().out
