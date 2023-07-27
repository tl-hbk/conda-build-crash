Should the call to `_collect_needed_dsos` still take `files` instead of `files_to_inspect`?

https://github.com/conda/conda-build/blob/655dbe1e6c760c95c329dc044ba94f753499b531/conda_build/post.py#L1455-L1462

In this [commit](https://github.com/conda/conda-build/commit/6deb528dd0d5ff76df9709f8a6081fe4f8ed189b) code was added 
to only check against platform specific filetypes but the call to `_collect_needed_dsos` didn't change.

https://github.com/conda/conda-build/blob/6deb528dd0d5ff76df9709f8a6081fe4f8ed189b/conda_build/post.py#L863-L871

https://github.com/conda/conda-build/blob/6deb528dd0d5ff76df9709f8a6081fe4f8ed189b/conda_build/post.py#L930-L940

I've run into an issue where a package I'm working on with a vendored 3rd party dependency has both .pyd and .so files 
and the process crashes when trying to inspect the .so file on windows using py-lief. 

https://github.com/conda/conda-build/blob/655dbe1e6c760c95c329dc044ba94f753499b531/conda_build/os_utils/liefldd.py#L357-L359

I've created a minimal reproduction of the issue with just one of the .pyd and .so files 