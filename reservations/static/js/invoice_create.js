// Basic reference data (e.g. client or invoice No.) 1 2 3 4 5 6
// Weights from right to left 1 3 7 1 3 7
// The sums arrived at are added together 1+6+21+4+15+42 = 89
// The following number ending in zero 90
// from which the added sum is subtracted -89
// Difference = check digit 1

function makeReferenceNumber(number) {
    var sum = 0;
    var weights = [7, 3, 1];

    for(var i = number.length - 1; i >= 0; i--) {
        sum += parseInt(number[i]) * weights[0];
        weights.push(weights.shift());
    }

    var difference = (Math.ceil(sum / 10) * 10) - sum;

    return number + difference.toString();
}