from statistics_class import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()

    for player in stats.matches(matcher):
        print(player)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(20, "assists"),
    #     PlaysIn("PHI")
    # )
    # matcher = And(
    #     HasFewerThan(2, "goals"),
    #     PlaysIn("NYR")
    # )

    # matcher = And(
    #     Not(HasAtLeast(2, "goals")),
    #     PlaysIn("NYR")
    # )
    # matcher = And(
    #     HasAtLeast(2, "goals"),
    #     PlaysIn("NYR")
    # )

    # matcher=Or(HasAtLeast(45, "goals"),
    #            HasAtLeast(70, "assists"))

    # matcher=And(HasAtLeast(70, "points"),
    #             Or(
    #                 PlaysIn("NYR"),
    #                 PlaysIn("FLA"),
    #                 PlaysIn("BOS")
    #             ))

    # for player in stats.matches(matcher):
    #     print(player)

    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all))


if __name__ == "__main__":
    main()
