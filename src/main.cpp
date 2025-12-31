#include <chrono>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <thread>
#include <vector>

namespace
{
struct CorruptionPhase
{
    std::string title;
    std::string description;
    int visualNoise;
};

class FacilityState
{
public:
    void advanceNight()
    {
        ++nightCount_;
        corruption_ = std::min(1.0, corruption_ + 0.18);
    }

    [[nodiscard]] int nightCount() const { return nightCount_; }
    [[nodiscard]] double corruption() const { return corruption_; }

private:
    int nightCount_ = 0;
    double corruption_ = 0.0;
};

class MenuRenderer
{
public:
    explicit MenuRenderer(const std::vector<CorruptionPhase>& phases) : phases_(phases) {}

    void drawBanner(double corruption) const
    {
        const int jagged = static_cast<int>(corruption * 10);
        std::cout << "\n=== THE ANOMLYS // NUTTY'INC FACILITY ===\n";
        std::cout << "Corruption: " << std::fixed << std::setprecision(2) << corruption * 100
                  << "%";
        std::cout << " (" << phaseFor(corruption).title << ")" << '\n';

        std::cout << "Glitch: ";
        for (int i = 0; i < 5 + jagged; ++i)
        {
            const char symbol = static_cast<char>('A' + (i + jagged) % 26);
            std::cout << (i % 2 == 0 ? symbol : '#');
        }
        std::cout << '\n';
    }

    void describePhase(double corruption) const
    {
        const auto phase = phaseFor(corruption);
        std::cout << "\nPhase: " << phase.title << '\n';
        std::cout << phase.description << "\n";
        std::cout << "Visual Noise Level: " << phase.visualNoise << '\n';
    }

    void drawOptions() const
    {
        std::cout << "\n1) Start next night";
        std::cout << "\n2) View corruption report";
        std::cout << "\n3) Multiplayer briefing";
        std::cout << "\n4) Quit";
        std::cout << "\nSelect: ";
    }

    void renderBriefing() const
    {
        std::cout << "\nMULTIPLAYER BRIEFING" << '\n';
        std::cout << "- Up to 4 players: 1 mascot handler, 1 engineer, 2 scouts." << '\n';
        std::cout << "- Handler distracts Nutty, engineer keeps generators stable." << '\n';
        std::cout << "- Scouts tag anomalies and route power cables across wings." << '\n';
        std::cout << "- Voice queues are role-based; downed players drop keycards." << '\n';
    }

private:
    CorruptionPhase phaseFor(double corruption) const
    {
        const int tier = static_cast<int>(corruption * phases_.size());
        const int index = std::min(static_cast<int>(phases_.size() - 1), tier);
        return phases_[index];
    }

    std::vector<CorruptionPhase> phases_;
};

class Night
{
public:
    explicit Night(int nightNumber, double corruption)
        : nightNumber_(nightNumber), corruption_(corruption)
    {
    }

    void play()
    {
        narrate("Spooling up cameras...", 500);
        narrate("Locking down Nutty'Inc facility." , 300);
        narrate("Loading mascot skin simulation layers...", 400);

        std::cout << "\nNight " << nightNumber_ << " begins.\n";

        runStep("Power reroute", "Engage backup relays before anomalies pop breakers.");
        runStep("Mascot containment", "Coordinate handler distraction while engineer stabilizes." );
        runStep("Corruption shielding", corruptionShielding());
        runStep("Extraction", "Race to the elevator while doors stutter from glitches." );

        std::cout << "\nNight " << nightNumber_ << " clear. Expect heavier corruption next night." << '\n';
    }

private:
    static void narrate(const std::string& line, int delayMs)
    {
        std::cout << line << '\n';
        std::this_thread::sleep_for(std::chrono::milliseconds(delayMs));
    }

    void runStep(const std::string& title, const std::string& description)
    {
        std::cout << "\n> " << title << '\n' << description << '\n';
        const int shards = 3 + static_cast<int>(corruption_ * 10);
        std::cout << "Visual shards: ";
        for (int i = 0; i < shards; ++i)
        {
            std::cout << (i % 2 == 0 ? '/' : '*');
        }
        std::cout << '\n';
    }

    std::string corruptionShielding() const
    {
        if (corruption_ < 0.2)
        {
            return "Seal vents with foam; corruption sheen is minimal.";
        }
        if (corruption_ < 0.5)
        {
            return "Deploy signal jammers; mascot audio bleeds through walls.";
        }
        if (corruption_ < 0.8)
        {
            return "Overlay AR blinders; staff cameras flicker with doppelgangers.";
        }
        return "Emergency: full blackout route while static claws at headset feed.";
    }

    int nightNumber_ = 0;
    double corruption_ = 0.0;
};

class Game
{
public:
    Game()
        : menuRenderer_({
              {"Stable", "Nutty's foam suit is pristine; echoes are just vents.", 1},
              {"Fractured", "Mascot decals peel. PA system stutters in reversed slogans.", 3},
              {"Hostile", "Holograms overlap the hallways. Mascot eyes track through cameras.", 6},
              {"Unbound", "Reality jitters. Elevators misroute. Power lines hum like teeth.", 9},
          })
    {
    }

    void run()
    {
        bool running = true;
        while (running)
        {
            menuRenderer_.drawBanner(facility_.corruption());
            menuRenderer_.drawOptions();

            std::string line;
            std::getline(std::cin, line);
            const int choice = parseChoice(line);

            switch (choice)
            {
            case 1:
                startNight();
                break;
            case 2:
                menuRenderer_.describePhase(facility_.corruption());
                break;
            case 3:
                menuRenderer_.renderBriefing();
                break;
            case 4:
                running = false;
                break;
            default:
                std::cout << "Invalid selection. Try again." << '\n';
                break;
            }
        }
    }

private:
    static int parseChoice(const std::string& line)
    {
        std::istringstream stream(line);
        int value = 0;
        stream >> value;
        return value;
    }

    void startNight()
    {
        facility_.advanceNight();
        Night night{facility_.nightCount(), facility_.corruption()};
        night.play();
    }

    FacilityState facility_;
    MenuRenderer menuRenderer_;
};
} // namespace

int main()
{
    std::cout << "Booting Nutty'Inc operations shell..." << '\n';
    std::cout << "The Anomlys is running as a C++ console prototype." << '\n';
    Game game;
    game.run();
    std::cout << "Facility shutdown complete." << '\n';
    return 0;
}
