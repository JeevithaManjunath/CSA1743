% hanoi(N, Source, Destination, Auxiliary)
% Solves the Towers of Hanoi problem for N disks.

hanoi(0, _, _, _) :- 
    % Base case: No move needed for 0 disks
    !.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 0,
    N1 is N - 1,
    
    % Step 1: Move N-1 disks from Source to Auxiliary
    hanoi(N1, Source, Auxiliary, Destination),

    % Step 2: Move the Nth (largest) disk from Source to Destination
    write('Move disk '), write(N),
    write(' from '), write(Source),
    write(' to '), write(Destination), nl,

    % Step 3: Move N-1 disks from Auxiliary to Destination
    hanoi(N1, Auxiliary, Destination, Source).
