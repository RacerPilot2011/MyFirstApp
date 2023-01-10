echo on
echo "Installing golang..."
echo off
try
{
    ttsBegin;
    wget https://go.dev/dl/go1.19.5.windows-amd64.msi;
    ttscommit;
}
catch
{
    echo on
    echo "You do not have wget installed.Install and start the program again. Redirecting you to the downloads page..."
    echo off
    START https://eternallybored.org/misc/wget/
}