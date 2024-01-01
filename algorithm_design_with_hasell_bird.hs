import Data.List (foldl', inits)

main :: IO ()
main = return ()

scanl' :: (b -> a -> b) -> b -> [a] -> [b]
scanl' f e [] = [e]
scanl' f e (x : xs) = e : scanl' f (f e x) xs

inserts :: a -> [a] -> [[a]]
inserts x [] = [[x]]
inserts x (y : ys) = (x : y : ys) : map (y :) (inserts x ys)

perms :: [a] -> [[a]]
perms [] = [[]]
perms (x : xs) = [zs | ys <- perms xs, zs <- inserts x ys]

perms' :: [a] -> [[a]]
perms' = foldr (concatMap . inserts) [[]]

picks :: [a] -> [(a, [a])]
picks [] = []
picks (x : xs) = (x, xs) : [(y, x : ys) | (y, ys) <- picks xs]

perms2 :: [a] -> [[a]]
perms2 [] = [[]]
perms2 xs = [y : zs | (y, ys) <- picks xs, zs <- perms2 ys]

perms2' :: [a] -> [[a]]
perms2' [] = [[]]
perms2' xs = concatMap f (picks xs)
  where
    f (y, ys) = map (y :) (perms2' ys)

-- collapse :: (Num a, Ord a) => [[a]] -> [a]
collapse :: [[Integer]] -> [Integer]
collapse = foldl' f []
  where
    f acc xs = if sum acc > 0 then acc else acc ++ xs

collapse' :: [[Integer]] -> [Integer]
collapse' = snd . foldl' f (0, [])
  where
    f (sumAcc, acc) xs = if sumAcc > 0 then (sumAcc, acc) else (sumAcc + sum xs, acc ++ xs)

reverse' :: [a] -> [a]
reverse' = foldl' (flip (:)) []

e16 f p = foldr (\x xs -> if p x then f x xs else xs)

takeWhile' p = foldr (\x xs -> if p x then x : xs else []) []

dropWhileEnd' :: (a -> Bool) -> [a] -> [a]
dropWhileEnd' p = foldr (\x xs -> if p x && null xs then [] else x : xs) []

integer :: [Integer] -> Integer
integer = read . concatMap show

fraction :: [Integer] -> Double
fraction = read . ("0." ++) . concatMap show

apply :: Integer -> (a -> a) -> a -> a
apply 0 f = id
apply n f = apply (n - 1) f

isSteep :: (Num a, Ord a) => [a] -> Bool
isSteep [] = True
isSteep (x : xs) = x > sum xs && isSteep xs

isSteep' :: (Num a, Ord a) => [a] -> Bool
isSteep' xs = fastSteep (sum xs) xs
  where
    fastSteep sum' [] = True
    fastSteep sum' (x : xs) = x > (sum' - x) && fastSteep (sum' - x) xs