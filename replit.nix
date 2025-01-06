{ pkgs }: {
    deps = [
        pkgs.python3
        pkgs.python310
        pkgs.python39
        pkgs.python38
        pkgs.python
        pkgs.pythonFull
        pkgs.python310Packages.http-server
        pkgs.nodejs-16_x
        pkgs.nodePackages.http-server
        pkgs.python3Packages.pip
    ];
    env = {
        PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            # Needed for pandas / numpy
            pkgs.stdenv.cc.cc.lib
        ];
        PYTHONBIN = "${pkgs.python3}/bin/python3";
        PYTHONBIN3 = "${pkgs.python3}/bin/python3";
        LANG = "en_US.UTF-8";
        STDERREDBIN = "${pkgs.stdenv.cc.cc}/bin/stderred";
        NODEJS_VERSION = "16.x";
    };
}
