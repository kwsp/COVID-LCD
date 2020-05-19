#!/bin/bash

WORKDIR=$(pwd)
UNITFILE="lcd.service"
SYSTEMD_DIR="/home/$USER/.config/systemd/user"
UNIT_FILE_TARGET=$SYSTEMD_DIR/$UNITFILE

install() {
    echo "Working directory: $WORKDIR"
    echo
    echo "Writing unit-file to $SYSTEMD_DIR/$UNITFILE"
    mkdir -p $SYSTEMD_DIR
    sed "s|WORKDIR_PLACEHOLDER|$WORKDIR|g" $UNITFILE > $UNIT_FILE_TARGET
    if [ $? != 0 ]; then 
        echo "Could not create unit file"
        return  1
    fi
    echo "Successfully created unit file"
    echo "Enabling LCD daemon"
    systemctl --user enable lcd
    systemctl --user start lcd
}

uninstall() {
    echo Removing unit file $UNIT_FILE_TARGET
    rm $UNIT_FILE_TARGET 2&>/dev/null
    if [ "$?" -eq 0 ]; then
        echo "File doesn't exist"
        return 0
    fi
    systemctl --user stop lcd 2&>/dev/null
    systemctl --user disable lcd 2&>/dev/null
}

main() {
    for arg in $@
    do
        if [ "$arg" = "-h" ] || [ "$arg" = "--help" ] ; then
            echo Usage: bla bla bla
            return 0
        elif [ "$arg" = "u" ] || [ "$arg" = "-u" ] || [ "$arg" = "--uninstall" ] ; then
            uninstall
            return 0
        fi
    done

    install
}

main $@
