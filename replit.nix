{ pkgs }: {
    deps = [
        pkgs.nodejs-16_x
        pkgs.nodePackages.http-server
    ];
    env = {
        NODEJS_VERSION = "16.x";
        LANG = "en_US.UTF-8";
    };
}
