@echo off
Rem SET /A --> set for variable, to call the variable must be open and close with %%
SET /A a = 5
SET /A b = 10
SET /A c = %a% + %b%
echo %c%