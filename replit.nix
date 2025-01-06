{ pkgs }: {
    deps = [
        pkgs.python310
        pkgs.python310Packages.http-server
    ];
    env = {
        PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            # Needed for pandas / numpy
            pkgs.stdenv.cc.cc.lib
        ];
        PYTHONBIN = "${pkgs.python310}/bin/python3.10";
        LANG = "en_US.UTF-8";
        STDERREDBIN = "${pkgs.stdenv.cc.cc}/bin/stderred";
    };
}
