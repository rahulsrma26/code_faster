Code Faster
===========

Cross-platform command line utility for bootstrapping online codes (especially codeforces) and running with automatic testing.


## Index

*	[Uses](#uses)
*	[Example](#example)
*   [Installing](#installing)
*   [Setting up with VSCode](#setup)

---

[](#uses)
## Uses

This package installs two commands:

* **cfetch**

    This will fetches the code from given url.
    ```sh
    usage: cfetch [-h] [-l {cpp,java,py}] [-d DIR] url
    positional arguments:
    url                   url of the code

    optional arguments:
    -h, --help                    show this help message and exit
    -l, --language {cpp,java,py}  default is cpp
    -d, --dir DIR             if given then uses this dir and language flag will be ignored.
    ```
    If dir is provided (language flag will be ignored) then it'll copy the contents of your sample dir into the created one. Using this you can use your own template for any language whatsoever. However, runner will still work only on supported languages.

    example:
    ```sh
    cfetch http://codeforces.com/problemset/problem/1/A
    ```
    This will create a folder named CF1-A in the current directory with sample test cases and main.cpp file.

* **crun**
    This will run the file and if there are test cases present in the file's directory it will run them too.
    ```sh
    crun <file-path> [args]
    ```
    Where args are compiler args for compiled languages like c++ and java.

    example:
    ```sh
    crun CF1-A\main.cpp
    ```
    This will create a folder for binaries in the file's directory with the output of sample tests. It will also generates the test report.

    You can manually create more test files.
    Supported formats are:
    | Input  | Output  |
    |--------|---------|
    | .i.txt | .o.txt  |
    | .i     | .o      |
    | .input | .output |

---

[](#example)
## Example

First we will fetch a problem from [codeforces.com](http://codeforces.com/problemset/problem/1/A)

```sh
> cfetch http://codeforces.com/problemset/problem/1/A
CF1-A created
test_1 created
main.cpp created
```

Now we will try to run it with our sample generated code.

```sh
> crun CF1-A\main.cpp
g++  -o CF1-A\bin\main.exe CF1-A\main.cpp
========================================
test_1 FAILED
---------------------------------------- [output]
6
---------------------------------------- [answer]
4
========================================
:( 0/1 passed.
```

Now fix the main.cpp file to solve the problem.
```cpp
int main() {
    using namespace std;

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m, a;
    cin >> n >> m >> a;

    int r = ((n + a - 1) / a) * ((m + a - 1) / a);
    cout << r << '\n';
}
```

```sh
> crun CF1-A\main.cpp
g++  -o CF1-A\bin\main.exe CF1-A\main.cpp
========================================
test_1 PASSED
========================================
:) 1/1 passed.
```

---

[](#installing)
## Installing

You can install from [pypi](https://pypi.org/project/code-faster/).
```sh
pip install code-faster -U
```

Or, you can install directly from the repository using pip.
```sh
pip install git+https://github.com/rahulsrma26/code_faster
```

---

[](#setup)
## Setting up with VSCode

You can set keyboard shortcuts to any editor basically. There are plenty of extensions in VSCode that can do that but for demonstration we will be using [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)

For code-runner, edit `settings.json` file in `.vscode` folder.
```json
{
    "code-runner.fileDirectoryAsCwd": true,
    "code-runner.runInTerminal": true,
    "code-runner.saveFileBeforeRun": true,
    "code-runner.executorMap": {
        "cpp": "crun $fileName",
        "java": "crun $fileName",
        "python": "crun $fileName"
    }
}
```

Now to run a file just open it and press
<kbd>control</kbd>+<kbd>option</kbd>+<kbd>n</kbd> (on mac)
or <kbd>control</kbd>+<kbd>alt</kbd>+<kbd>n</kbd> (on pc).

Note: If you are using `conda` environments and if it's not added to the path environments (or bash). Then `crun` may be unaccessible in the terminal by default. So, you either need to activate it in the terminal, or you need to update the shell args.

```json
"terminal.integrated.shellArgs.windows": ["/K", "<conda-install-path>/Scripts/activate && conda activate <your-env>"]
```
For linux you can change `terminal.integrated.shellArgs.linux` and for mac change `terminal.integrated.shellArgs.osx`
