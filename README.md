# Android automation exercise

**Archived — no longer maintained.** This repository preserves a Python/Appium test assignment
from 2022 using pytest and the Page Object pattern. The dependencies and application under test
are historical; compatibility with current Appium and Android versions is not maintained.

- Test scenarios: [cases.txt](cases.txt)
- Test implementation: [src/tests](src/tests)
- Page objects: [src/AppPages.py](src/AppPages.py)
- Original dependencies: [Pipfile](Pipfile) and [requirements.txt](requirements.txt)
- Original application package: `test.apk`

The original environment used a Pixel 4 emulator with Android API 30, a 1080 × 2280 screen
(393 × 830 dp), and a configured Appium server. The original test command was `pytest`.
