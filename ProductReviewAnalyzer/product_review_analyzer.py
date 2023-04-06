from marvin import Bot

class ProductReviewAnalyzer:
    def __init__(self):
        self.bot = Bot(
            name="ProductReviewAnalyzer",
            instructions=("Extract product reviews from a website, "
                          "analyze them and provide a summary of overall customer sentiment.")
        )

    async def extract_summary(self, website_url):
        result = await self.bot.say(f"Visit this website '{website_url}' and analyze the sentiment of the reviews")
        return result.content


async def main():
    analyzer = ProductReviewAnalyzer()
    website_url = "https://www.nike.com/mx/t/calzado-de-carrera-en-carretera-vaporfly-2-dxSLFw/CU4111-401"

    summary = await analyzer.extract_summary(website_url)
    print(summary)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
