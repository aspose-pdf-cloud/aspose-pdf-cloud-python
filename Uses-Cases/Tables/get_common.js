// 1. Load your Application Secret and Key from the JSON file or set credentials in another way
// 2. Create an object to connect to the Pdf.Cloud API
// 3. Upload your document file
// 4. Perform the retreiving link annotattions from Pdf document using getPageLinkAnnotations() function
// 5. Check result and perform some actions with result.body object
// 6. Create a new Link Annotation with the required properties
// 7. Append new Link Annotation to the document using postPageLinkAnnotations() function
// 8. Perform some action after successful addition
// All values of variables starting with "YOUR_****" should be replaced by real user values

import credentials from "./../../credentials.json"  with { type: "json" };
import fs from 'node:fs/promises';
import path from 'node:path';
import { PdfApi } from "./../../src/api/api.js";
import { Table } from "../../src/models/table.js";
import { Cell } from "../../src/models/cell.js";
import { FontStyles } from "../../src/models/fontStyles.js";
import { GraphInfo } from "../../src/models/graphInfo.js";
import { Row } from "../../src/models/row.js";
import { TextRect } from "../../src/models/textRect.js";

const configParams = {
    LOCAL_PATH: "C:\\Samples\\",

    PDF_DOCUMENT_NAME: "sample.pdf",

    LOCAL_RESULT_DOCUMENT_NAME: "output_sample.pdf",

    PAGE_NUMBER: 2,     // Your document page number...

    TABLE_ID: "GE5TCOZSGAYCYNRQGUWDINZVFQ3DGMA",
};

const pdfApi = new PdfApi(credentials.id, credentials.key);

const pdfTables = {
    uploadFiles: async function (fileName) {
        const pdfFileData = await fs.readFile(configParams.LOCAL_PATH + fileName);
        await pdfApi.uploadFile(fileName, pdfFileData);
    },

    downloadFiles: async function (local_path, fileName) {
        const changedPdfData = await pdfApi.downloadFile(configParams.PDF_DOCUMENT_NAME);

        const filePath = path.join(local_path, fileName);

        await fs.writeFile(filePath, changedPdfData.body);
        console.log("downloaded: " + filePath);
    },

    uploadDocument: async function () {
        await pdfTables.uploadFiles(configParams.PDF_DOCUMENT_NAME);
    },

    getAllTables: async function () {
        const resultTabs = await pdfApi.getDocumentTables(configParams.PDF_DOCUMENT_NAME);

        if (resultTabs.body.code == 200 && resultTabs.body.tables) {
            if (!Array.isArray(resultTabs.body.tables.list) || resultTabs.body.tables.list.length === 0) {
                throw new Error("Unexpected error : tables is null or empty!!!");
            }
            pdfTables.showTablesInfo(resultTabs.body.tables.list, "all");
            return resultTabs.body.tables.list;
        }
        else
            throw new Error("Unexpected error : can't get tables!!!");
    },

    getTableById: async function () {
        const resultTabs = await pdfApi.getTable(configParams.PDF_DOCUMENT_NAME, configParams.TABLE_ID);

        if (resultTabs.body.code == 200 && resultTabs.body.table) {
            pdfTables.showTablesInfo( [ resultTabs.body.table ], "byId");
            return resultTabs.body.table;
        }
        else
            throw new Error("Unexpected error : can't get tables!!!");
    },

    initTable: function () {
        const numOfCols = 5;
        const numOfRows = 5;

        const headerTextState = {
            font: "Arial Bold",
            fontSize: 11,
            foregroundColor: { a: 0xFF, r: 0xFF, g: 0xFF, b: 0xFF },
            fontStyle: FontStyles.Bold,
            fontFile: null,
            underline: false,
            strikeOut: false,
            superscript: false,
            subscript: false,
        };

        const commonTextState = {
            font: "Arial Bold",
            fontSize: 11,
            foregroundColor: { a: 0xFF, r: 0x70, g: 0x70, b: 0x70 },
            fontFile: null,
            underline: false,
            strikeOut: false,
            superscript: false,
            subscript: false,
        };
    
        const table = new Table();
        table.rows = [];
    
        let colWidths = "";
        for (let c = 0; c < numOfCols; c++)
        {
            colWidths += " 70";
        }
    
        table.columnWidths = colWidths;
    
        const borderTableBorder = new GraphInfo();
        borderTableBorder.color = { a: 0xFF, r: 0x00, g: 0xFF, b: 0x00 };
        borderTableBorder.lineWidth = 0.5;
    
        table.defaultCellBorder = {
            top: borderTableBorder,
            right: borderTableBorder,
            bottom: borderTableBorder,
            left: borderTableBorder,
            roundedBorderRadius: 0
        };
        table.left = 150;
        table.top = 250;
    
        for (let r = 0; r < numOfRows; r++)
        {
            const row = new Row();

            row.cells = [];
    
            for (let c = 0; c < numOfCols; c++)
            {
                const cell = new Cell();
                
                cell.defaultCellTextState = commonTextState;

                if (r == 0)  // header cells
                {
                    cell.backgroundColor = { a: 0xFF, r: 0x80, g: 0x80, b: 0x80 };
                    cell.defaultCellTextState = headerTextState;
                }
                else {
                    cell.backgroundColor = { a: 0xFF, r: 0xFF, g: 0xFF, b: 0xFF };
                };
              
                const textRect = new TextRect();
                if (r == 0)
                    textRect.text = "header #" + c;
                else
                    textRect.text = "value";
                cell.paragraphs = [textRect];

                row.cells.push(cell);
            }
            table.rows.push(row);
        }
        return table;
    },

    addTableOnPage: async function (pageNum) {
        const jsonTable = pdfTables.initTable();

        const resultTabs = await pdfApi.postPageTables(configParams.PDF_DOCUMENT_NAME, pageNum, [ jsonTable ]);

        if (resultTabs.body.code == 200) {
            console.log("Table successfully added!");
            return resultTabs.body.table;
        }
        else
            throw new Error("Unexpected error : can't get tables!!!");
    },

    showTablesInfo: function(tables, prefix) {
        if (Array.isArray(tables) && tables.length > 0)
        {
            tables.forEach(function(table) {
                console.log(prefix +" => id: '" + table.id + "', page: '" + table.pageNum + "', rows: '" + table.rowList.length + "'");
            });
        }
        else
            console.error("showTablesInfo() error: array of tables is empty!")
    },
}

export default pdfTables;

await (async () => {
    await pdfTables.uploadDocument();
    await pdfTables.getAllTables();
    await pdfTables.getTableById();
    await pdfTables.addTableOnPage(configParams.PAGE_NUMBER);
    await pdfTables.downloadFiles( configParams.LOCAL_PATH, configParams.LOCAL_RESULT_DOCUMENT_NAME );
})().catch((error) => { console.log(error.message); });