#!/bin/ruby

t = gets.strip.to_i

for a0 in (0..t-1)
    n = gets.strip.to_i-1

    seriesSum = lambda { |x| (x * (x + 1)) / 2 }
    sum = 3*seriesSum.call(n/3) + 5*seriesSum.call(n/5) - 15*seriesSum.call(n/15)
    print sum
end
