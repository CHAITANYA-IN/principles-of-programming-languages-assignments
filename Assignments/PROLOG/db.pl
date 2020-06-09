% Knowledge Base :
airport(toronto, 50, 60).
airport(london, 75, 80).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(malaga, 50, 30).
airport(valencia, 40, 20).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

plane(toronto, 'air canada', london, 500, 360).
plane(toronto, united, london, 650, 420).
plane(toronto, 'air canada', madrid, 900, 480).
plane(toronto, united, madrid, 950, 540).
plane(toronto, iberia, madrid, 800, 480).
plane(madrid, 'air canada', barcelona, 100, 60).
plane(madrid, iberia, barcelona, 120, 65).
plane(madrid, iberia, valencia, 40, 20).
plane(london, iberia, barcelona, 220, 240).
plane(barcelona, iberia, valencia, 110, 75).
plane(madrid, iberia, malaga, 50, 60).
plane(malaga, iberia, valencia, 80, 120).
plane(paris, united, toulouse, 35, 120).

flight(A, B, C, D, E) :- plane(A, B, C, D, E).
clausea(A, C) :- (plane(A, B, C, D, E); plane(C, B, A, D, E)).
clauseb(A, B, C, D, E) :- (plane(A, B, C, D, E); plane(C, B, A, D, E)), D < 400.
clausec(A, B, C, D, E) :- (plane(A, F, C, D, E); plane(A, F, C, D, E)), (plane(B, F, G, D, E); plane(B, F, G, D, E)).
claused(A, B, C, D, E) :- clauseb(A, B, C, D, E); plane(A, 'air canada', C, D, E).
clausee(A, B) :- ((plane(A, united, B, _, _); plane(B, united, A, _, _)) -> (plane(B, 'air canada', A, _, _); plane(A, 'air canada', B, _, _))).