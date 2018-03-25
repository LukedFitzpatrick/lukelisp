let "failCount = 0";
let "passCount = 0";


tput setaf 4; echo "==="

for filename in tests/*.ll; do
    echo "Running test $filename..."
    python src/lukelisp.py $filename > $filename.actual;

    DIFF=$(diff $filename.actual $filename.expected)
    if [ "$DIFF" != "" ] 
    then
	tput setaf 1; echo "        Failed!";
	let "failCount=failCount+1";
    else
	tput setaf 2; echo "        Passed!";
	let "passCount=passCount+1";
    fi
done

tput setaf 4; echo "==="

tput setaf 1; echo "Fail count: $failCount"
tput setaf 2; echo "Pass count: $passCount"


