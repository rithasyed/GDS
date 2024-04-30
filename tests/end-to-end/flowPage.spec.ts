import { Page, test } from "@playwright/test";

test.describe("Flow Page tests", () => {
  async function goToFlowPage(page: Page) {
    await page.goto("http:localhost:3000/");
    await page.getByRole("button", { name: "New Project" }).click();
  }

  test("save", async ({ page }) => {
    await page.goto("http:localhost:3000/");
    await page.waitForTimeout(2000);

    await page.locator('//*[@id="new-project-btn"]').click();
    await page.waitForTimeout(1000);

    await page.getByTestId("blank-flow").click();
    await page.waitForTimeout(1000);
    await page.getByTestId("extended-disclosure").click();
    await page.getByPlaceholder("Search").click();
    await page.getByPlaceholder("Search").fill("custom");

    await page.waitForTimeout(1000);

    await page
      .locator('//*[@id="helpersCustom Component"]')
      .dragTo(page.locator('//*[@id="react-flow-id"]'));
    await page.mouse.up();
    await page.mouse.down();
    await page
      .locator('//*[@id="react-flow-id"]/div[1]/div[2]/button[2]')
      .click();

    await page
      .locator('//*[@id="react-flow-id"]/div[1]/div[2]/button[2]')
      .click();

    await page
      .locator('//*[@id="react-flow-id"]/div[1]/div[2]/button[2]')
      .click();
    // await page.getByTestId("icon-ExternalLink").click();
    // await page.locator('//*[@id="checkAndSaveBtn"]').click();
  });
});
