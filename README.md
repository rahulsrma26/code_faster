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
    cfetch <code-url> [language]
    ```
    Where language can be one of:

    * cpp (default)
    * java
    * py

    example:
    ```sh
    cfetch http://codeforces.com/problemset/problem/1/A cpp
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


[](#example)
## Example

First we will fetch a problem from [codeforces.com](http://codeforces.com/problemset/problem/1/A)

```sh
> cfetch http://codeforces.com/problemset/problem/1/A cpp
CF1-A created
test_1 created
main.cpp created
```

Now we will try to run it with out sample generated code.
```sh
>crun CF1-A\main.cpp
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
>crun CF1-A\main.cpp
g++  -o CF1-A\bin\main.exe CF1-A\main.cpp
========================================
test_1 PASSED
========================================
:) 1/1 passed.
```

[](#installing)
## Installing

```sh
pip install https://github.com/rahulsrma26/code_faster
```

[](#setup)
## Setting up with VSCode


